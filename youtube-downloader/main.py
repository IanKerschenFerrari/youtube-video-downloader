# pip install pytube
import pytube

video_url = input("Enter video URL: ")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download(input('enter directory: '))