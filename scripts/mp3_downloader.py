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
    with open('us_spotify_responses.json', 'w') as f:
        output = {}
        output['data'] = responses
        output['date-retrieved'] = time
        json.dump(output, f, indent=2)

def download_us_mp3():
    error = 0
    with open('us-chart.json', 'r') as f:
        data = json.load(f)
        chart = data['us-chart']
        for song in chart:
            url = full_url(song['spotifyID'])
            r = requests.get(url).json()
            try:
                preview_url = r['preview_url']
                # print "-"*50
                # print "has preview_url"
                # song_title = song['title'].split(' ')
                # file_name = "-".join(song_title) + '.mp3'
                # print file_name
            except Exception as e:
                error += 1
                print "-"*50
                print "no preview_url"
                song_title = song['title'].split(' ')
                file_name = "-".join(song_title) + '.mp3'
                print file_name
        print "No. of no preview_url:", error

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
