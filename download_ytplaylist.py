#!/usr/bin/env python3

import argparse
import os
import sys

try:
    import yt_dlp
except Exception as e:
    print("yt_dlp module is not installed.")
    raise SystemExit(1) from e

def download_playlist(url, dir, audio_only=False, max_count=None):
    os.makedirs(dir, exist_ok=True)
    
    if audio_only: format = "bestaudio/best"
    else: format = "bestvideo+bestaudio/best"
    
    ydl_opts = {
        "outtmpl": os.path.join(dir, "%(playlist_index)s - %(title)s.%(ext)s"),
        "ignoreerrors": True,
        "quiet": True,
        "no_warnings": True,
        "format": format,
        "preferredcodec": "mp4",
    }
    
    if audio_only:
        ydl_opts.update({
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        })
    
    if max_count is not None:
        ydl_opts["playlistend"] = max_count

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downloads a YouTube playlist.")
    parser.add_argument("url", type=str, help="URL of the YouTube playlist to download")
    parser.add_argument(
        "--dir", type=str, default=".", help="Directory to save the Videos"
    )
    parser.add_argument(
        "--audio-only", action="store_true", help="Download audio only"
    )
    parser.add_argument(
        "--max-count", type=int, default=None, help="Maximum number of videos to download"
    )

    args = parser.parse_args()

    try:
        download_playlist(args.url, args.dir, args.audio_only)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
