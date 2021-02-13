from tkinter import *

root = Tk()

def callback():
    print('Hello World!')

menubar = Menu(root)
menubar.add_command(label = 'Undo', command = callback)
menubar.add_command(label = 'Redo', command = callback)

frame = Frame(root, width = 512, height = 512)
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)

frame.bind('<Button-2>', popup)

root.mainloop()