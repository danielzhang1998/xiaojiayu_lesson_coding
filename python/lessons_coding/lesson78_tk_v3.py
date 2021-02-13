from tkinter import *
from tkinter import colorchooser

root = Tk()

def callback():
    fileName = colorchooser.askcolor()
    print(fileName)

Button(root, text = 'Choose the color', command = callback).pack()

root.mainloop()