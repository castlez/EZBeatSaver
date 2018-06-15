from urllib.request import Request, urlopen
import zipfile

import os

from tkinter import *


def get_song(url):
    if url == "q":
        return 0

    filepath = "D:\\Steam\\SteamApps\\common\\Beat Saber\\CustomSongs\\"
    tempname = url.split("=")[1]
    filename = filepath + tempname + ".zip"
    temp = os.path.join(filepath, tempname)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    with open(filename, 'wb') as out_file:
        out_file.write(webpage)

    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(temp)
    zip_ref.close()

    final_name = filepath + os.listdir(temp)[0]
    os.rename(temp, os.path.join(filepath, final_name))

    os.remove(temp + ".zip")
    return 1


def callback():
    url = str(E1.get())
    if url.strip() == '':
        return
    get_song(url)
    E1.delete(0, 'end')


top = Tk()
top.title("EZBeatSaver")
top.geometry("250x50")

L1 = Label(top, text="Song URL")
L1.grid(row=0, column=0)

E1 = Entry(top, bd = 5)
E1.grid(row=0, column=1)

MyButton1 = Button(top, text="Get that bitch", width=10, command=callback)
MyButton1.grid(row=1, column=1)

top.mainloop()
