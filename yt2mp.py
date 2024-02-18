import subprocess
import sys
import os
from tqdm import tqdm  # Import tqdm for the progress bar

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
                # Use tqdm for progress bar for both mp3 and mp4
                with tqdm(desc=f"Downloading {url} as {format_choice.upper()}", unit="B", unit_scale=True) as progress_bar:
                    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                    progress_bar.update(1)
                print(f"Downloaded {url} as {format_choice.upper()} with a progress bar.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to download {url} as {format_choice.upper()}: {e}")

file_name = input("Enter the name of the file containing the URLs: ")
file_path = file_name.strip()

output_folder = "yt2media"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Folder '{output_folder}' created successfully!")

while True:
    format_choice = input("Enter 'mp3' or 'mp4' to specify the format to download: ").lower()
    if format_choice in ['mp3', 'mp4']:
        break
    else:
        print("Invalid format choice. Please enter 'mp3' or 'mp4'.")

download_urls_from_file(file_path, output_folder, format_choice)
