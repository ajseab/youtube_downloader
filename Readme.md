# YouTube Video Downloader

This is a simple command-line tool written in Python for downloading YouTube videos. It allows you to easily save videos from YouTube to your local machine.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:

   ```shell
   pip install pytube
   ```

## Usage

1. Open a terminal and navigate to the directory where the code files are located.

2. Run the script with the following command:

   ```shell
   python3 youtube_downloader.py [YouTube Video URL]
   ```

   Replace `[YouTube Video URL]` with the URL of the YouTube video you want to download.

3. The script will download the video in the highest available resolution and save it to your current directory.

## Configuration

In the code, there is a variable named `DOWNLOAD_PATH` that specifies the download location for the videos. You can modify this variable to set a custom download path.

## Notes

- Ensure that you have a stable internet connection before running the script.
- This script uses the `pytube` library to interact with YouTube's API and retrieve video data.
- The downloaded video will be saved with the title of the video as the filename.
- This code is currently designed to work on any platform that supports Python 3.x.
- In case of RegexMatchError replace: 
      'cypher.py' line 30: var_regex = re.compile(r"^\w+\W")
            with         : var_regex = re.compile(r"^\$*\w+\W")

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the BSD-4-Clause (LICENSE).
```