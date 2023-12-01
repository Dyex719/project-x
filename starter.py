from yt_dlp.extractor.youtube import YoutubeIE
from yt_dlp import YoutubeDL
import pickle

URLS = ['https://www.youtube.com/watch?v=TIOZUdc0aL8']

youtube_downloader = YoutubeDL()

yt_extractor = YoutubeIE(youtube_downloader)
extracted_info = yt_extractor.extract(URLS[0])

# print(extracted_info['heatmap'])
pickle_file_path = 'data.pkl'

# Write the data to the pickle file
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(extracted_info['heatmap'], pickle_file)

#TODO: find the heatmap part of the dictionary