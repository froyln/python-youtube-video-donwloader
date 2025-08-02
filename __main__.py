import subprocess
import os

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def clear_console():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')

def title():
    print("__   __          _         _           ______                    _                 _           ")
    print("\ \ / /         | |       | |          |  _  \                  | |               | |          ")
    print(" \ V /___  _   _| |_ _   _| |__   ___  | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print("  \ // _ \| | | | __| | | | '_ \ / _ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print("  | | (_) | |_| | |_| |_| | |_) |  __/ | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print("  \_/\___/ \__,_|\__|\__,_|_.__/ \___| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|")
    print("by froyln")
    print("----------------------------------------------------------------------------------------------")
    print("Note: This program requires yt-dlp and ffmpeg to be installed.")
    print("Credit to yt-dlp for downloading videos and ffmpeg for merging audio and video.")
    print("----------------------------------------------------------------------------------------------")

clear_console()
title()

if not check_ffmpeg():
    print("ffmpeg is not installed or not found in PATH. Please install ffmpeg for merging video and audio.")
    print("You can download it from https://ffmpeg.org/download.html")
    print("After installing, make sure ffmpeg is in your system PATH.")
    print("Exiting the program.")
    exit(1)

def download_video(): 
    try: 
        if quality == "best":
            format_code = "bestvideo+bestaudio[ext=m4a]/best"
            subprocess.run(["yt-dlp", "-f", format_code, "--merge-output-format", "mp4", url], check=True)
            print("Download completed successfully.")
            exit(1)
        else:
            format_code = f"bestvideo[height<={quality}]+bestaudio[ext=m4a]/best[height<={quality}]"
            subprocess.run(["yt-dlp", "-f", format_code, "--merge-output-format", "mp4", url], check=True)
            print("Download completed successfully.")
            exit(1)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to download the video: {e}")
        print("Make sure you have yt-dlp installed and the URL is correct.")
        print("You want retry the download with a valid URL? (y/n)")
        retry = input().strip().lower()
        if retry != 'y':
            exit(1)
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it using 'pip install yt-dlp'.")
        exit(1)

def download_audio(): 
    try: 
        if quality == "best":
            format_code = "bestaudio[ext=m4a]/best"
            subprocess.run(["yt-dlp", "-f", format_code, url], check=True)
            print("Download completed successfully.")
            exit(1)
        else:
            format_code = f"bestaudio[ext=m4a]/best[height<={quality}]"
            subprocess.run(["yt-dlp", "-f", format_code, url], check=True)
            print("Download completed successfully.")
            exit(1)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to download the video: {e}")
        print("Make sure you have yt-dlp installed and the URL is correct.")
        print("You want retry the download with a valid URL? (y/n)")
        retry = input().strip().lower()
        if retry != 'y':
            exit(1)
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it using 'pip install yt-dlp'.")
        exit(1)

while True:
    print("Insert the URL of the YouTube video you want to download:")
    url = input().strip()
    print("Enter the desired quality (e.g., 720, 1080) or press Enter for best available:")
    quality = input().strip()
    if not quality:
        quality = "best"
    print("You set the quality to:", quality)
    print("You want to download the video or audio? (v/a)")
    choice = input().strip().lower()
    if choice == 'v':
        print("Downloading video with audio...")
        download_video()
    elif choice == 'a':
        print("Downloading audio only...")
        download_audio()
    else:
        print("Invalid choice. Please enter 'v' for video or 'a' for audio.")
        continue
