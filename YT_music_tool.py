import os
import glob
from pytube import YouTube
from pydub import AudioSegment

def download_song():
    #downloads the song from youtube in mp4 format
    video_to_download = input('insert the link of the youtube song that you want to download: ')
    YouTube(video_to_download).streams.first().download()
    yt = YouTube(video_to_download)
    video= yt.streams.filter(progressive=True, file_extension='mp4').first()
    destination = "temp_audio"

    #converts the file into mp3 format
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    audio = AudioSegment.from_file(out_file)
    mp3_file = base + '.mp3'
    audio.export(mp3_file,format='mp3')

    #deletes the original mp4 file
    os.remove(out_file)

    #asks if you want to download more songs
    question = input('do you want to download another song? Yes/No? ' )
    if question == 'yes':
        download_song()
    else:
        exit()

download_song() 
