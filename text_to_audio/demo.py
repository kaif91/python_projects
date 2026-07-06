import os
from gtts import gTTS
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

def text_to_audio():
    text = entry.get()
    langauge = 'en'
    output =gTTS(text=text,lang=langauge,slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")

entry = Entry(root)
canvas.create_window(200,180,window=entry)
button = Button(text="start",command=lambda:text_to_audio())
canvas.create_window(200,230,window=button)

root.mainloop()