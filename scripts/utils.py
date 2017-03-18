import json


def toSongDict(song):
    obj = {}
    obj['title'] = song.title
    obj['artist'] = song.artist
    obj['peakPos'] = song.peakPos
    obj['lastPos'] = song.lastPos
    obj['weeks'] = song.weeks
    obj['rank'] = song.rank
    obj['change'] = song.change
    obj['spotifyID'] = song.spotifyID
    obj['spotifyLink'] = song.spotifyLink
    obj['videoLink'] = song.videoLink
    return obj


def read_from_json(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def write_to_json(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)
