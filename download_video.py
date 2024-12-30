import yt_dlp


def download_video(url):
    # Options for yt-dlp to select the best quality video and audio and merge them into a single MP4 file
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best',  # Download the best video with a max height of 720p and best audio
        'outtmpl': '%(title)s.%(ext)s',  # Save file with the video title
        'noplaylist': True,  # If the URL is a playlist, it will download only the first video
        'merge_output_format': 'mp4',  # Ensure that the merged output is in MP4 format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Use FFmpeg to convert video if necessary
            'preferedformat': 'mp4',  # Convert to MP4 format
        }],
        'postprocessor_args': [
            '-c:v', 'libx264',  # Use the x264 codec for video
            '-c:a', 'aac',      # Use the AAC codec for audio
            '-strict', 'experimental',  # Allow experimental features in FFmpeg (necessary for certain conversions)
        ],
        'prefer_ffmpeg': True,  # Use FFmpeg for post-processing (merging and format conversion)
        'ffmpeg_location': 'C:\\ffmpeg\\bin',  # Ensure the location of FFmpeg (adjust if necessary)
    }

    # Using yt-dlp to download and convert the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Replace with the YouTube URL you want to download
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
    print("Download complete!")