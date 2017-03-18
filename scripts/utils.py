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
