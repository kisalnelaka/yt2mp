# yt2mp: YouTube Downloader with GUI

This Python code creates a user-friendly GUI-based YouTube downloader application using the `Tkinter` library and leverages the `youtube-download-cli` tool for video downloads.

## Features

- **Batch download:** Efficiently download multiple videos from a text file containing YouTube URLs.
- **Format selection:** Choose MP3 or MP4 as the desired output format.
- **Output folder management:** Automatically create the output folder if it doesn't exist or allow manual selection.
- **Error handling:** Provide informative messages for potential errors during download attempts.
- **Clear instructions:** Include comments and docstrings to enhance code readability and understanding.

## Requirements

- Python 3
- `tkinter` library (usually included in standard Python installations)
- `youtube-download-cli` (external tool): https://github.com/yt-dlp/yt-dlp

## Installation

1. **Clone this repository:**

   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/yt2mp
Use code with caution.
Navigate to the project directory:

Bash
cd yt2mp
Use code with caution.
Install required libraries:

Bash
pip install -r requirements.txt
Use code with caution.
Usage
Run the script:

Bash
python yt2mp.py
Use code with caution.
Select the file containing YouTube URLs: Click the "Browse" button next to the "Select the file containing the URLs:" label.

Choose the output folder: Click the "Browse" button next to the "Select the output folder:" label.

Select the download format: Choose either "MP3" or "MP4" using the radio buttons.

Start the download: Click the "Download" button.

Code Structure
Here's a breakdown of the code's organization:

1. download_urls_from_file function:

Reads URLs from the specified file.
Iterates through each URL and constructs the youtube-download-cli command with the selected format and output folder.
Executes the command using subprocess.run, handling potential errors and providing feedback.
2. YouTubeDownloaderGUI class:

Creates the main application window using Tkinter.
Initializes GUI elements like labels, entry fields, buttons, and radio buttons.
Binds events to buttons for browsing file selection, downloading, and managing output folder.
Implements the download method to trigger the download_urls_from_file function with user-selected options.
License
This code is licensed under the MIT License. See the LICENSE file for details.

Enhancements
While this code provides a functional YouTube downloader, consider these potential improvements:

Progress bar: Add a progress bar or status updates to indicate download progress.
Download queue: Allow adding multiple files or URLs for sequential downloading.
Advanced options: Explore providing more control over youtube-download-cli options like bitrate or video quality.
Error handling refinement: Handle more specific error scenarios and provide more tailored feedback.
I hope this comprehensive presentation helps you understand and use the code effectively!