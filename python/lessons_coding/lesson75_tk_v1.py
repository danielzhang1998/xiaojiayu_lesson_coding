from tkinter import *

root = Tk()

def callback(event):
    print('position: ', event.x, event.y)

frame = Frame(root, width = 200, height = 200)
frame.bind('<Button-1>', callback)
frame.pack()

mainloop()