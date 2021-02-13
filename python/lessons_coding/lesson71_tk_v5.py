from tkinter import *
import hashlib

root = Tk()

new_text = Text(root, width = 30, height = 10, undo = True, autoseparators = False)
new_text.pack()

new_text.insert(INSERT, 'I love FishC.com!')

def callback(event):
    new_text.edit_separator()

new_text.bind('<Key>', callback)

Button(root, text = 'Undo', command = new_text.edit_undo).pack()

mainloop()