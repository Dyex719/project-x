from yt_dlp.extractor.youtube import YoutubeIE
from yt_dlp import YoutubeDL
import pickle
import matplotlib.pyplot as plt
import pickle
from scipy.signal import find_peaks
import numpy as np
import yt_dlp
import yt_dlp.utils

# URLS = ['https://www.youtube.com/watch?v=TIOZUdc0aL8']

URLS = [
    "http://www.youtube.com/watch?v=JTpDCoxZdv8",
    "http://www.youtube.com/watch?v=sDOlpRJMcQI",
    "http://www.youtube.com/watch?v=AXSm49NGkg8",
    "http://www.youtube.com/watch?v=8dwrE0OCq40",
    "http://www.youtube.com/watch?v=2a34XyiZO14"
]

youtube_downloader = YoutubeDL()

yt_extractor = YoutubeIE(youtube_downloader)
extracted_info = yt_extractor.extract(URLS[0])

# print(extracted_info['heatmap'])
pickle_file_path = 'data.pkl'

# Write the data to the pickle file
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(extracted_info['heatmap'], pickle_file)

data = extracted_info['heatmap']

time_points = [entry['start_time'] for entry in data] + [data[-1]['end_time']]
values = [entry['value'] for entry in data] + [data[-1]['value']]

# Create a numpy array for time_points and values
time_array = np.array([0.0] + time_points)
values_array = np.array([0.0] + values)
# Define the interval duration
interval_duration = 10.0  # seconds
peaks, _ = find_peaks(values_array, height=0.0, distance = interval_duration)
combined = [list(x) for x in zip(values_array[peaks], time_array[peaks])]
combined.sort()
print(combined)


def download_sections(*ranges):
    def inner(info_dict, ydl):
        for idx, (start, end) in enumerate(ranges):
            yield {
                'start_time': start,
                'end_time': end,
                'index': idx
            }
    return inner

def download_sections(ranges):
    def inner(info_dict, ydl):
        for idx, (start, end) in enumerate(ranges):
            yield {
                'start_time': start,
                'end_time': end,
                'index': idx
            }
    return inner

width = 2.5
time_intervals = [[time_ - width//2, time_ + width//2] for _, time_ in combined[:4]]
time_intervals.append([0.0, width])
ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # help(yt_dlp.postprocessor) 
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
    'download_ranges': download_sections(time_intervals),
    'outtmpl': 'songs/%(title)s/Hint#%(section_number)s %(title)s %(section_start)s-%(section_end)s [%(id)s].%(ext)s'
    # 'download_ranges': yt_dlp.utils.download_range_func([1,2,3,4,5], time_intervals),
    # 'outtmpl': '%(title)s %(section_start)s-%(section_end)s [%(id)s] %(section_number)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
