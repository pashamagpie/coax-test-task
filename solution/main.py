import os.path
import requests
from moviepy.editor import VideoFileClip


# 1st Task
s = "Python Bootcamp"
hashed_string = hash(s)


# 2nd Task
def convert_to_gif(url: str):
    """
    Convert video from given URL to GIF image

    :param url: URL to video
    :return: filepath to GIF image
    """
    r = requests.get(url, stream=True)
    with open('video_to_convert.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=256):
            f.write(chunk)
    video = VideoFileClip('video_to_convert.mp4')
    video.write_gif('converted.gif')
    return os.path.abspath('converted.gif')
