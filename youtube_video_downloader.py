import os

import pytube


# specify the YouTube video URL
video_url = "https://www.youtube.com/embed/<code>"
from pytube.exceptions import VideoUnavailable


def video_downloader(url,folder):
    # create a YouTube object from the URL
    yt = pytube.YouTube(url)

    # select the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # download the stream
    if not os.path.exists(folder+'//'+yt.title+'.mp4'):
        print(f'{yt.title} downloading....')
        stream.download(folder)
        print(f'{yt.title} downloaded')
    else:
        print(f'{yt.title} already available')


video_downloader(video_url, outputFolder)
