from wsgiref import validate

import bcrypt
from tkinter import *

def validate(password):
    #123456
    hashed = b'$2b$12$yL6i.4CgYqLoi8VL41t/m.E6tNrv1J7bCsshu/COIRR.PReZw.qEm'
    entered_password = bytes(password,"utf-8")
    if bcrypt.checkpw(entered_password, hashed):
        print("Valid password")
    else:
        print("Invalid password")
root = Tk()
root.geometry("300x300")
password_entry = Entry(root)
password_entry.pack()

button = Button(root, text="Validate", command=lambda:validate(password_entry.get()))
button.pack()

root.mainloop()