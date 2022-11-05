from tkinter import *
from pytube import YouTube 
from pytube.cli import on_progress
import os

class main:

    root = Tk()
    root.geometry('400x202')
    root.resizable(0, 0)
    root.title('Youtube downloader by Francisco')
    status1 = 'Downloaded Successfully'

class dowload:

    def dowload():

        link = interface.form.get()
        url = YouTube(link, on_progress_callback = on_progress)
        interface.status["text"] = main.status1
        os.chdir('videos')

        yd = url.streams.get_highest_resolution()
        yd.download()

class interface:

    texto = Label(main.root, text="Download videos from Youtube").pack(pady=30)

    form = Entry(main.root)
    form.pack(ipadx=60)

    Button(main.root, text="Dowload", command=dowload.dowload).pack(pady=10)

    legen = Label(main.root, text="Status:")
    legen.pack(pady=10)

    status = Label(main.root, text="")
    status.pack()


main.root.mainloop()
