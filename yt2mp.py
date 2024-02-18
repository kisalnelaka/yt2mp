import subprocess
import sys
import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, Radiobutton, messagebox

def download_urls_from_file(file_path, output_folder, format_choice):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        urls = [url.strip() for url in urls if url.strip()]

        if not urls:
            messagebox.showinfo("Error", "No URLs found in the file.")
            return

        for url in urls:
            command = f'youtube-download-cli "{url}" {format_choice} -o "{output_folder}"'

            try:
                subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                print(f"Downloaded {url} as {format_choice.upper()} successfully.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to download {url} as {format_choice.upper()}: {e}")
            except KeyboardInterrupt:
                messagebox.showinfo("Info", f"Download of {url} as {format_choice.upper()} interrupted.")
                return

        messagebox.showinfo("Info", "Download completed.")

class YouTubeDownloaderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Downloader")

        self.file_label = Label(master, text="Select the file containing the URLs:")
        self.file_label.pack()

        self.file_entry = Entry(master, state='disabled', width=40)
        self.file_entry.pack(side='left')

        self.browse_button = Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack(side='left', padx=5)

        self.output_folder_label = Label(master, text="Select the output folder:")
        self.output_folder_label.pack()

        self.output_folder_entry = Entry(master, state='disabled', width=40)
        self.output_folder_entry.pack(side='left')

        self.browse_output_button = Button(master, text="Browse", command=self.browse_output_folder)
        self.browse_output_button.pack(side='left', padx=5)

        self.format_label = Label(master, text="Select the format to download:")
        self.format_label.pack()

        self.format_var = StringVar()
        self.format_var.set("mp3")  # Default format
        self.mp3_radio = Radiobutton(master, text="MP3", variable=self.format_var, value="mp3")
        self.mp3_radio.pack(side='left')
        self.mp4_radio = Radiobutton(master, text="MP4", variable=self.format_var, value="mp4")
        self.mp4_radio.pack(side='left')

        self.download_button = Button(master, text="Download", command=self.download)
        self.download_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.file_entry.config(state='normal')
        self.file_entry.delete(0, 'end')
        self.file_entry.insert(0, file_path)
        self.file_entry.config(state='disabled')

    def browse_output_folder(self):
        output_folder = filedialog.askdirectory()
        self.output_folder_entry.config(state='normal')
        self.output_folder_entry.delete(0, 'end')
        self.output_folder_entry.insert(0, output_folder)
        self.output_folder_entry.config(state='disabled')

    def download(self):
        file_path = self.file_entry.get().strip()
        output_folder = self.output_folder_entry.get().strip()
        format_choice = self.format_var.get().lower()

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            download_urls_from_file(file_path, output_folder, format_choice)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()
