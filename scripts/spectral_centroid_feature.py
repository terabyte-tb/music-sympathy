from glob import glob
from librosa.feature import spectral_centroid
from utils import read_from_json, write_to_json

import codecs
import json
import librosa
import sys


# return nth_track, track_name (with space)
def extract_track_name(track):
    only_file_name = track.split('/')[-1]
    nth_track = int(only_file_name.split('-')[0])
    track_name = ' '.join(only_file_name.split('.')[0].split('-')[1:])
    return nth_track, track_name


def get_files_centroid(tracks):
    output_tracks = {}
    for track in tracks:
        y, sr = librosa.load(track)
        centroid = spectral_centroid(y, sr)
        nth_track, track_name = extract_track_name(track)
        output_tracks[nth_track] = centroid
    return output_tracks


def write_centroid_to_json(tracks, region):
    json_file = {
        "us": "data/us.json",
        "uk": "data/uk.json",
        "jp": "data/jp.json"
    }
    selected_json = json_file[region]
    input_json = read_from_json(selected_json)
    files_centroid = get_files_centroid(tracks)
    for obj in input_json:
        position = obj['position']
        obj['centroid'] = files_centroid[position].tolist()
    # write_to_json(input_json, selected_json)
    json.dump(
                input_json,
                codecs.open(
                    selected_json,
                    'w',
                    encoding='utf-8'
                ),
                separators=(',', ':'),
                sort_keys=True,
                indent=2
    )  # this saves the array in .json format


def main():
    argc = len(sys.argv)
    if argc == 1:
        print("Please specify regions")
        print("US, UK, JP")
        sys.exit(0)
    else:
        region = sys.argv[1]
        if region.lower() == 'us':
            tracks = glob('tracks/us/*.mp3')
            write_centroid_to_json(tracks, region.lower())
        elif region.lower() == 'uk':
            tracks = glob('tracks/uk/*.mp3')
            write_centroid_to_json(tracks, region.lower())
        elif region.lower() == "jp":
            tracks = glob('tracks/jp/*.mp3')
            write_centroid_to_json(tracks, region.lower())
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
