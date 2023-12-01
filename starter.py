from yt_dlp.extractor.youtube import YoutubeIE
from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=TIOZUdc0aL8']

youtube_downloader = YoutubeDL()

yt_extractor = YoutubeIE(youtube_downloader)
extracted_info = yt_extractor.extract(URLS[0])

print(extracted_info)


#TODO: find the heatmap part of the dictionary