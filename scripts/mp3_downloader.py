from utils import read_from_json, write_to_json

import arrow
import csv
import json
import requests
import sys

spotifyURL = 'https://api.spotify.com/v1/tracks/'


def full_url(track_id):
    return spotifyURL + track_id


def save_spotify_responses(csv_file, output_file):
    with open(csv_file, 'r') as csv_f:
        charts = csv.DictReader(csv_f)
        responses = []
        time = arrow.now().isoformat()
        for song in charts:
            track_id = song['URL'].split('/')[-1]
            url = full_url(track_id)
            r = requests.get(url).json()
            responses.append(r)
    output = {}
    output['data'] = responses
    output['date-retrieved'] = time
    write_to_json(output, output_file)


def download_jp_mp3():
    data = read_from_json('jp_spotify_responses.json')
    songs = data['data']
    n = 100
    has_no_preview_url = 0
    for song in songs[:n]:
        preview_url = song['preview_url']
        if preview_url is None:
            print(song['name'])
            has_no_preview_url += 1
            continue
        else:
            file_name = '-'.join(song['name'].split(' ')) + '.mp3'
            file_path = "tracks/jp/"
            full_path = file_path + file_name
            r = requests.get(preview_url, stream=True)
            # Taken from
            # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
            with open(full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        # f.flush() commented by recommendation from J.F.Sebastian
    print("Total songs that has no preview_url:", has_no_preview_url)


def download_uk_mp3():
    data = read_from_json('uk_spotify_responses.json')
    songs = data['data']
    n = 100
    has_no_preview_url = 0
    for song in songs[:n]:
        preview_url = song['preview_url']
        if preview_url is None:
            print(song['name'])
            has_no_preview_url += 1
            continue
        else:
            file_name = '-'.join(song['name'].split(' ')) + '.mp3'
            file_path = "tracks/uk/"
            full_path = file_path + file_name
            r = requests.get(preview_url, stream=True)
            # Taken from
            # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
            with open(full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        # f.flush() commented by recommendation from J.F.Sebastian
    print("Total songs that has no preview_url:", has_no_preview_url)


def download_us_mp3():
    data = read_from_json('us_spotify_responses.json')
    songs = data['data']
    n = 100
    has_no_preview_url = 0
    for song in songs[:n]:
        preview_url = song['preview_url']
        if preview_url is None:
            print(song['name'])
            has_no_preview_url += 1
            continue
        else:
            file_name = '-'.join(song['name'].split(' ')) + '.mp3'
            file_path = "tracks/us/"
            full_path = file_path + file_name
            r = requests.get(preview_url, stream=True)
            # Taken from
            # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
            with open(full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        # f.flush() commented by recommendation from J.F.Sebastian
    print("Total songs that has no preview_url:", has_no_preview_url)


def main():
    argc = len(sys.argv)
    if argc == 1:
        print("Please specify regions")
        print("US, UK, JP")
        sys.exit(0)
    else:
        region = sys.argv[1]
        if region.lower() == 'us':
            download_us_mp3()
        elif region.lower() == 'uk':
            download_uk_mp3()
        elif region.lower() == "jp":
            download_jp_mp3()
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
