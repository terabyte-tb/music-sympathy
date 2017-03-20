from bpm_extract import get_file_bpm
from glob import glob

import csv
import sys


# return nth_track, track_name (with space)
def extract_track_name(track):
    only_file_name = track.split('/')[-1]
    nth_track = int(only_file_name.split('-')[0])
    track_name = ' '.join(only_file_name.split('.')[0].split('-')[1:])
    return nth_track, track_name


def get_files_bpm(tracks):
    output_tracks = {}
    for track in tracks:
        bpm = get_file_bpm(track)
        nth_track, track_name = extract_track_name(track)
        output_tracks[nth_track] = {"bpm": bpm, "track": track_name}
    return output_tracks


def write_bpm_to_csv(tracks, region):
    files_bpm = get_files_bpm(tracks)
    regions = {
        "us": "charts/regional-us-daily-latest.csv",
        "uk": "charts/regional-uk-daily-latest.csv",
        "jp": "charts/regional-jp-daily-latest.csv"
    }
    output_csv = {
        "us": "data/us.csv",
        "uk": "data/uk.csv",
        "jp": "data/jp.csv"
    }
    selected_region = regions[region]
    selected_output_csv = output_csv[region]
    with open(selected_region, 'r') as input_f:
        charts = csv.DictReader(input_f)
        with open(selected_output_csv, 'w') as output_f:
            fieldnames = ["Position", "Track Name", "Artist", "BPM", "Region"]
            writer = csv.DictWriter(output_f, fieldnames=fieldnames)
            writer.writeheader()
            for row in charts:
                position = int(row['Position'])
                if position > 100:
                    break
                file_bpm = files_bpm[position]["bpm"]
                writer.writerow(
                    {
                        "Position": position,
                        "Track Name": row['Track Name'],
                        "Artist": row['Artist'],
                        "BPM": file_bpm,
                        "Region": region.upper()
                    }
                )


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
            write_bpm_to_csv(tracks, region.lower())
        elif region.lower() == 'uk':
            tracks = glob('tracks/uk/*.mp3')
            write_bpm_to_csv(tracks, region.lower())
        elif region.lower() == "jp":
            tracks = glob('tracks/jp/*.mp3')
            write_bpm_to_csv(tracks, region.lower())
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
