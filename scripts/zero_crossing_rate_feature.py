from glob import glob
from librosa.feature import zero_crossing_rate
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


def get_files_zero_crossing_rate(tracks):
    output_tracks = {}
    for track in tracks:
        y, sr = librosa.load(track)
        zero_crossing = zero_crossing_rate(y)
        nth_track, track_name = extract_track_name(track)
        output_tracks[nth_track] = zero_crossing
    return output_tracks


def write_zero_crossing_rate_to_json(tracks, region):
    json_file = {
        "us": "data/us.json",
        "uk": "data/uk.json",
        "jp": "data/jp.json"
    }
    selected_json = json_file[region]
    input_json = read_from_json(selected_json)
    files_zero_crossing_rate = get_files_zero_crossing_rate(tracks)
    for obj in input_json:
        position = obj['position']
        obj['zero_crossing_rate'] = files_zero_crossing_rate[position].tolist()
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
            write_zero_crossing_rate_to_json(tracks, region.lower())
        elif region.lower() == 'uk':
            tracks = glob('tracks/uk/*.mp3')
            write_zero_crossing_rate_to_json(tracks, region.lower())
        elif region.lower() == "jp":
            tracks = glob('tracks/jp/*.mp3')
            write_zero_crossing_rate_to_json(tracks, region.lower())
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
