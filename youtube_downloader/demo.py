from tkinter import *
from tkinter import filedialog, messagebox
from urllib.parse import urlparse

try:
    import yt_dlp
except ImportError:
    yt_dlp = None

try:
    from pytube import YouTube
except ImportError:
    YouTube = None


def get_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)


def is_valid_youtube_url(url):
    try:
        parsed = urlparse(url)
        return parsed.scheme in {"http", "https"} and any(
            host in parsed.netloc for host in ("youtube.com", "youtu.be")
        )
    except Exception:
        return False

def download():
    video_url = url_entry.get().strip()
    output_dir = path_label.cget("text")

    if not is_valid_youtube_url(video_url):
        messagebox.showerror("Invalid URL", "Please enter a valid YouTube URL.")
        return

    if output_dir == "Select path to download":
        messagebox.showerror("Download Path", "Please select a folder to save the video.")
        return

    try:
        if yt_dlp is not None:
            options = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
                "noplaylist": True,
                "quiet": True,
                "merge_output_format": "mp4",
                "ffmpeg_location": r"C:\Users\Downloads\ffmpeg-master-latest-win64-gpl-shared\bin",
            }
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([video_url])
        elif YouTube is not None:
            # pytube fallback for environments without yt-dlp.
            YouTube(video_url).streams.get_highest_resolution().download(output_path=output_dir)
        else:
            messagebox.showerror(
                "Missing dependency",
                "Install yt-dlp or pytube to download videos:\npip install yt-dlp",
            )
            return

        messagebox.showinfo("Success", "Video downloaded successfully.")
    except Exception as exc:
        messagebox.showerror(
            "Download failed",
            f"Could not download this video.\n{exc}\n\nTip: Install/update yt-dlp with\npip install -U yt-dlp",
        )


root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=420, height=300)
canvas.pack()

app_label = Label(root,text="Video downloader",fg="blue",font=("Arial",20))
canvas.create_window(200,20,window=app_label)

url_label = Label(root,text="Enter video url")
url_entry = Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

#path to download videos
path_label = Label(root,text="Select path to download")
path_button = Button(root,text="Select",command=get_path)
canvas.create_window(200,150,window=path_label)
canvas.create_window(200,170,window=path_button)

download_button = Button(root,text="Download",command=download)
canvas.create_window(200,250,window=download_button)
root.mainloop()