from pytube.cli import on_progress
from pytube import YouTube
from pytube import Playlist
import os

option = input("Choose an option (video or playlist): ")
resolution = input("Please choose the resolution (360p or 720p): ")
downloadpath = input("Please enter download path: ")

def finish():
    print("Video downloaded.")
        
if option == "playlist":

    playlist_link = input("Please enter playlist's URL: ")
    playlist = Playlist(playlist_link)
                
    for yt in playlist.videos:
        if resolution == "720p":
            yt.streams\
            .get_highest_resolution()\
            .download(output_path=downloadpath)
        
        else:
            yt.streams\
            .get_lowest_resolution()\
            .download(output_path=downloadpath)
          
else:

    video_link = input("Please enter video's URL: ")
    yt = YouTube(video_link, on_progress_callback=on_progress)
       
if resolution == "720p":  
    yt.streams\
    .get_highest_resolution()\
    .download(output_path=downloadpath)
    
else:
    yt.streams\
    .get_lowest_resolution()\
    .download(output_path=downloadpath)
yt.register_on_complete_callback(finish())
