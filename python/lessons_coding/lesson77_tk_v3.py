from tkinter import *

root = Tk()

Label(root, text = 'User name').grid(row = 0, padx = 5, pady = 5, sticky = W)
Entry(root).grid(row = 0, column = 1, padx = 5, pady = 5)

Label(root, text = 'Password').grid(row = 1, padx = 5, pady = 5, sticky = W)
Entry(root, show = '*').grid(row = 1, column = 1, padx = 5, pady = 5)


root.mainloop()