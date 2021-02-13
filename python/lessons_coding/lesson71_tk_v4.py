from tkinter import *
import hashlib

root = Tk()

new_text = Text(root, width = 30, height = 10)
new_text.pack()

new_text.insert(INSERT, 'I love FishC.com!')

start = '1.0'

while True:
    pos = new_text.search('o', start, stopindex = END)
    if not pos:
        break
    else:
        array = []     
        array.extend([int(pos.split('.')[0]), int(pos.split('.')[1])])
        t = tuple(array)
        print('the position:', t)
        start = pos + '+1c'
mainloop()