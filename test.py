from pytube import YouTube
import re

stream_res_list = []

try:
    video_url = f"https://www.youtube.com/watch?v=-gJ1a4qzO58"
    yt = YouTube(video_url)

    streams = yt.streams.filter(progressive=True)
    avail_res_list = []
    for i, stream in enumerate(streams):
        match = re.search(r"\d+(?=p)", stream.resolution)
        stream_res = int(match.group())
        avail_res_list.append(stream_res)
    stream_res_list.append(max(avail_res_list))
except Exception as e:
    # Skip this video if the 'streamingData' key is not present
    stream_res_list.append(0)

print(stream_res_list)