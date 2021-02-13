from tkinter import *

root = Tk()

w = Spinbox(root, from_=0, to = 10, increment = 0.1, wrap = True)
w.pack(padx = 10, pady = 10)

q = Spinbox(root, values = ('A','B','C','D','E','F','G'), wrap = True)
q.pack(padx = 10, pady = 10)
root.mainloop()