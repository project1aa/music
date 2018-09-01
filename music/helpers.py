from mutagen.mp3 import MP3
from datetime import timedelta


def get_filesize(filename):
    try:
        audio = MP3(filename)
        length = audio.info.length
        td = str(timedelta(seconds=length))
        tds = td.split(':')
        minutes = tds[1]
        seconds = tds[2].split('.')[0]
        return '{}:{}'.format(minutes, seconds)
    except FileNotFoundError:
        raise ValidationError('Found Not Found')
