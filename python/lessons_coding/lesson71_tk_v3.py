from tkinter import *
import hashlib

root = Tk()

new_text = Text(root, width = 30, height = 10)
new_text.pack()

new_text.insert(INSERT, 'I love FishC.com!')

contents = new_text.get('1.0', END)

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents = new_text.get('1.0', END)
    if sig != getSig(contents):
        print('thing has been modify')
    else:
        print('nothing happend!')

Button(root, text = 'check it!', command = check).pack()

mainloop()