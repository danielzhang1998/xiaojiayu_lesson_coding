from tkinter import *

root = Tk()

w = Canvas(root, width = 1000, height = 500, background = 'lightgray')
w.pack(padx = 10, pady = 10)

w.create_line(0, 250, 1000, 250, fill='black')
w.create_line(500, 0, 500, 500, fill='black', dash = (4, 4))
w.create_rectangle(250, 125, 750, 375, fill='white')

mainloop()