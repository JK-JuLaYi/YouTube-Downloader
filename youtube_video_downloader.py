import os

import pytube
import pandas as pd

# specify the YouTube video URL
# video_url = "https://www.youtube.com/embed/S06jHWa7Brk"
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

def list_videos():
    # replace 'file_path' with the path of the Excel workbook you want to read
    file_path = "F:\\AI\\Speak\\urls.xlsx"

    # read all sheets of the Excel workbook into a dictionary of data frames
    sheets_dict = pd.read_excel(file_path , sheet_name=None, header=None)
    # print(sheets_dict)

    # loop through the dictionary and print the name and contents of each sheet
    for sheet_name, sheet_data in sheets_dict.items():
        new_folder = os.getcwd()+'\\Videos\\'+sheet_name
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        for links in sheet_data.iloc[:,0]:
            # print(links)
            try:
                video_downloader(links,new_folder)
            except VideoUnavailable:
                pass

        # print(sheet_data)


list_videos()