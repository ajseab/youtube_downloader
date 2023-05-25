# ---------------------------------
# Title: YouTube Downloader for MacOS
# Author: A. Seabolt
#
# Pass YouTube URL as argument when running this script and it will be
# downloaded into the provided path. 
# ---------------------------------

# Import statements
import ssl
import sys
from pytube import YouTube

# Create a download path variable
# Must replace with your path
DOWNLOAD_PATH = "/Users/user/Downloads"

# Needed to verofy certificates otherwise you will recieve a urlopen error
ssl._create_default_https_context = ssl._create_stdlib_context

# Records a list of arguments from the terminal
SYS_ARGUMENTS = sys.argv

# Gets the Youtube link from argument when running youtube_downloader.py
# Example: ~ python3 youtube_downloader.py https://youtube.com/video
# "https://youtube.com/video" is recorded in yt_link
YT_LINK = str(SYS_ARGUMENTS[1])

# Creates a yt object from YouTube with the provided link
# Uses oauth and allows oauth cache
try:
    yt = YouTube(
    YT_LINK,
    use_oauth = True,
    allow_oauth_cache = True
    )
except:
    print("Connection Error")

# Set the file name of the video
FILE_NAME = yt.title.replace(" ", "_")
FILE_NAME = FILE_NAME.lower()
FILE_NAME += ".mp4"

try:
    stream = yt.streams.get_highest_resolution() # Gets the highest resolution mp4 available for download
    stream.download(DOWNLOAD_PATH, FILE_NAME) # Downloads the video
except:
    print("Some Error.")

print(f"Downloaded {FILE_NAME} to /Users/avery/Downloads")
