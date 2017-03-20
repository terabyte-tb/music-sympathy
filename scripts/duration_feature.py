from utils import read_from_json

import pandas as pd
import sys


def write_duration_to_csv(songs, region):
    input_csv = {
        "us": "data/us.csv",
        "uk": "data/uk.csv",
        "jp": "data/jp.csv"
    }
    selected_input_csv = input_csv[region]
    csv_input = pd.read_csv(selected_input_csv)
    durations = []
    n = 100
    for song in songs[:n]:
        duration_ms = song['duration_ms']
        durations.append(duration_ms)
    csv_input['duration_ms'] = durations
    csv_input.to_csv(selected_input_csv, index=False)


def main():
    argc = len(sys.argv)
    if argc == 1:
        print("Please specify regions")
        print("US, UK, JP")
        sys.exit(0)
    else:
        region = sys.argv[1]
        if region.lower() == 'us':
            data = read_from_json("spotify-responses/us_spotify_responses.json")
            songs = data['data']
            write_duration_to_csv(songs, region.lower())
        elif region.lower() == 'uk':
            data = read_from_json("spotify-responses/uk_spotify_responses.json")
            songs = data['data']
            write_duration_to_csv(songs, region.lower())
        elif region.lower() == "jp":
            data = read_from_json("spotify-responses/jp_spotify_responses.json")
            songs = data['data']
            write_duration_to_csv(songs, region.lower())
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
