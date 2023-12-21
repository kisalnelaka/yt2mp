import subprocess
import sys
import os
import time

def check_install_youtube_download_cli():
    try:
        subprocess.run(["youtube-download-cli", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("youtube-download-cli is already installed.")
    except subprocess.CalledProcessError:
        install_youtube_download_cli()

def install_youtube_download_cli():
    print("Installing youtube-download-cli...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "youtube-download-cli"], check=True)
        print("youtube-download-cli installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install youtube-download-cli: {e}")
        sys.exit(1)

def download_urls_from_file(file_path, output_folder, format_choice):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        urls = [url.strip() for url in urls if url.strip()]

        if not urls:
            print("No URLs found in the file.")
            return

        for url in urls:
            command = f'youtube-download-cli "{url}" {format_choice} -o "{output_folder}"'
            try:
                subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                print(f"Downloaded {url} as {format_choice.upper()}.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to download {url} as {format_choice.upper()}: {e}")

file_name = input("Enter the name of the file containing the URLs: ")
file_path = file_name.strip()

output_folder = "yt2media"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Folder '{output_folder}' created successfully!")

# Prompt the user to select the format
while True:
    format_choice = input("Enter 'mp3' or 'mp4' to specify the format to download: ").lower()
    if format_choice in ['mp3', 'mp4']:
        break
    else:
        print("Invalid format choice. Please enter 'mp3' or 'mp4'.")

# Check and install youtube-download-cli if necessary
check_install_youtube_download_cli()

# Then continue with the rest of the script, specifying the output folder and format
download_urls_from_file(file_path, output_folder, format_choice)
