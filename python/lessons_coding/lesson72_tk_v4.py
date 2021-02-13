from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width = 1000, height = 500)
w.pack()

center_x = 500
center_y = 250
r = 250

points = [
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    center_x - int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
    center_x,
    center_y - r,
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5))
]

w.create_polygon(points, outline = 'black', fill = 'gray')

mainloop()