from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty
from subprocess import run, CalledProcessError

class DownloadButton(Button):
    format = StringProperty()

class DownloaderApp(App):
    url_input = StringProperty()
    output_folder = StringProperty()
    selected_format = StringProperty()
    download_progress = StringProperty("0%")

    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20)

        # URL input
        url_label = Label(text="Enter YouTube URL:")
        self.url_input = TextInput(multiline=False)
        layout.add_widget(url_label)
        layout.add_widget(self.url_input)

        # Output folder selection
        output_label = Label(text="Output Folder:")
        output_button = Button(text="Select Folder")
        output_button.bind(on_press=self.open_filechooser)
        layout.add_widget(output_label)
        layout.add_widget(output_button)
        self.output_folder = ""

        # Format dropdown
        format_label = Label(text="Format:")
        format_dropdown = DropDown()
        for format in ["mp3", "mp4"]:
            btn = DownloadButton(text=format, format=format)
            btn.bind(on_press=self.format_selected)
            format_dropdown.add_widget(btn)
        format_button = Button(text="Select Format")
        format_button.bind(on_press=format_dropdown.open)
        layout.add_widget(format_label)
        layout.add_widget(format_button)

        # Download button
        download_button = Button(text="Download")
        download_button.bind(on_press=self.download_video)
        layout.add_widget(download_button)

        # Progress bar
        self.progress_bar = ProgressBar(max=100)
        layout.add_widget(self.progress_bar)

        return layout

    def open_filechooser(self, instance):
        # Implement filechooser using Kivy's FileChooser and update self.output_folder
        pass

    def format_selected(self, instance):
        self.selected_format = instance.format

    def download_video(self, instance):
        if not all([self.url_input, self.output_folder, self.selected_format]):
            print("Please fill in all fields.")
            return

        command = f'youtube-download-cli "{self.url_input}" {self.selected_format} -o "{self.output_folder}"'

        try:
            process = run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = process.stdout.decode("utf-8")
            print(output)
            # Update progress bar based on output (if possible)
        except CalledProcessError as e:
            print(f"Failed to download: {e}")

        # Reset progress bar and UI state

if __name__ == "__main__":
    DownloaderApp().run()
