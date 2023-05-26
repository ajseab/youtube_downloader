#!/usr/bin/env python3

"""A YouTube video downloader for MacOS
"""

# Import statements
import ssl
import sys
from pytube import YouTube

def main():
    # Create a download path variable
    # Must replace with your path
    download_path = "/Users/avery/Downloads"

    # Needed to verofy certificates otherwise you will recieve a urlopen error
    ssl._create_default_https_context = ssl._create_stdlib_context

    # Records a list of arguments from the terminal
    sys_args = sys.argv

    # Gets the Youtube link from argument when running youtube_downloader.py
    # Example: ~ python3 youtube_downloader.py https://youtube.com/video
    # "https://youtube.com/video" is recorded in yt_link
    yt_link = str(sys_args[1])

    # Creates a yt object from YouTube with the provided link
    # Uses oauth and allows oauth cache
    try:
        yt = YouTube(
        yt_link,
        use_oauth = True,
        allow_oauth_cache = True
        )
    except:
        print("Connection Error")

    # Set the file name of the video
    file_name = yt.title.replace(" ", "_")
    file_name = file_name.lower()
    file_name += ".mp4"

    try:
        stream = yt.streams.get_highest_resolution() # Gets the highest resolution mp4 available for download
        stream.download(download_path, file_name) # Downloads the video
    except:
        print("Some Error.")

    print(f"Downloaded {file_name} to {download_path}")
    
if __name__ == "__main__":
    main()