import pytube
from os import getcwd
url=input('Enter url:')
youtube=pytube.YouTube(url)
video=youtube.streams.get_audio_only()
video.download(getcwd())