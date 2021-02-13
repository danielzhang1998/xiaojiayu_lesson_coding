from tkinter import *
from tkmacosx import Button as button

root = Tk()

w = Canvas(root, width = 1000, height = 500, background = 'lightgray')
w.pack(padx = 10, pady = 10)



button(root, text = 'delete all', command = (lambda x = ALL: w.delete(x)), bg = 'lightblue').pack(pady = 10)

mainloop()