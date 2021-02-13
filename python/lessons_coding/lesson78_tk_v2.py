from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('200x200')
def callback():
    fileName = filedialog.askopenfilename()
    print(fileName)

Button(root, text = 'Open the file', command = callback).pack()

root.mainloop()