from utils import read_from_json, write_to_json

import arrow
import json
import requests
import sys

spotifyURL = 'https://api.spotify.com/v1/tracks/'


def full_url(track_id):
    return spotifyURL + track_id


def save_spotify_responses():
    with open('us-chart.json', 'r') as f:
        data = json.load(f)
        chart = data['us-chart']
        responses = []
        time = arrow.now().isoformat()
        for song in chart:
            url = full_url(song['spotifyID'])
            r = requests.get(url).json()
            responses.append(r)
    output = {}
    output['data'] = responses
    output['date-retrieved'] = time
    output_file = "us_spotify_responses.json"
    write_to_json(output, output_file)


def download_us_mp3():
    data = read_from_json('us_spotify_responses.json')
    songs = data['data']
    for song in songs:
        if u'error' in song.keys():
            continue
        preview_url = song['preview_url']
        if preview_url is None:
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


def main():
    argc = len(sys.argv)
    if argc == 1:
        print "Please specify regions"
        print "US, TH, JP"
        sys.exit(0)
    else:
        region = sys.argv[1]
        if region.lower() == 'us':
            download_us_mp3()
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
