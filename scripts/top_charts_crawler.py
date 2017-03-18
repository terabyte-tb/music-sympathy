from utils import toSongDict, write_to_json

import arrow
import billboard
import json
import sys


def getUSTopChart():
    chart = billboard.ChartData('hot-100')
    time = arrow.now().isoformat()
    songs = []
    for song in chart:
        song_dict = toSongDict(song)
        songs.append(song_dict)
    output = {}
    output['us-chart'] = songs
    output['date-retrieved'] = time
    output_file = "us-chart.json"
    write_to_json(output, output_file)


def main():
    argc = len(sys.argv)
    if argc == 1:
        print "Please specify regions"
        print "US, TH, JP"
        sys.exit(0)
    else:
        region = sys.argv[1]
        if region.lower() == 'us':
            getUSTopChart()
        else:
            raise NotImplementedError


if __name__ == '__main__':
    main()
