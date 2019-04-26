import youtube_dl
import tkinter as tk


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '$HOME/Música/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),

}


def musicDownloader(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(url)])


def gui():
    root = tk.Tk()
    root.title('youtube-dl Music Downloader Interface')
    fr = tk.Frame(root)
    fr.pack(fill='both', expand=True)
    root.geometry('600x100')

    lbl1 = tk.Label(fr, text='URL', fg='blue', font='Roboto, 16')
    lbl1.pack()

    e1 = tk.Entry(fr, width=60, font='Roboto')
    e1.pack()

    btn1 = tk.Button(fr, text='Download', width=8, font=12, command=lambda: musicDownloader(e1.get()))
    btn1.pack()

    root.mainloop()


def main():
    gui()


if __name__ == "__main__":
    main()
