# YouTube Video Downloader with yt-dlp

This Python project allows you to download YouTube videos and merge the best quality video and audio into a single MP4 file using the `yt-dlp` library and FFmpeg.

## Features

- Downloads the best video with a maximum height of 720p.
- Merges the best available audio with the video.
- Converts the video and audio into a single MP4 file.
- Customizable output file name based on the video title.
- Supports FFmpeg post-processing for video/audio merging and conversion.
- Provides a simple command-line interface for entering video URLs.

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (a fork of youtube-dl)
- [FFmpeg](https://ffmpeg.org/) (for video/audio processing)

### Install dependencies

1. **Install yt-dlp**:
    ```bash
    pip install yt-dlp
    ```

2. **Install FFmpeg**:
    - Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
    - Make sure to add FFmpeg to your system's PATH or specify its location in the `ffmpeg_location` option in the script.

## How to Use

1. Clone this repository or download the `download_video.py` file.

2. Run the Python script:

    ```bash
    python download_video.py
    ```

3. Enter the YouTube video URL when prompted:

    ```bash
    Enter the YouTube video URL: https://www.youtube.com/watch?v=YOUR_VIDEO_ID
    ```

4. The script will download the best video and audio, merge them, and save them as an MP4 file with the video title.

## Customization

You can customize the download options in the `ydl_opts` dictionary:

- Change the video quality by adjusting the `'format'` option.
- Modify the output filename template using the `'outtmpl'` option.
- Adjust FFmpeg settings for codec selection, bitrate, etc., via `'postprocessor_args'`.

## Example Script

```python
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best',  # Best video quality (max 720p)
        'outtmpl': '%(title)s.%(ext)s',  # Output filename as video title
        'noplaylist': True,  # Only download the first video (not playlist)
        'merge_output_format': 'mp4',  # Ensure the output is in MP4 format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'postprocessor_args': [
            '-c:v', 'libx264',  # Use x264 codec for video
            '-c:a', 'aac',      # Use AAC codec for audio
            '-strict', 'experimental',  # Allow experimental features in FFmpeg
        ],
        'prefer_ffmpeg': True,  # Use FFmpeg for merging and conversion
        'ffmpeg_location': 'C:\\ffmpeg\\bin',  # Specify FFmpeg location (adjust if necessary)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
    print("Download complete!")
```

## License

This project is open-source and available under the MIT License. Feel free to contribute or modify it as needed.

---
Created with love by Harivansh Bhardwaj

If you encounter any issues or have suggestions for improvements, feel free to open an issue or pull request. Happy downloading!