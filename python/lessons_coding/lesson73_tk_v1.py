from tkinter import *
from tkmacosx import Button as button

root = Tk()

w = Canvas(root, width = 400, height = 200)
w.pack()

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1,y1,x2,y2, fill = 'black')

w.bind('<B1-Motion>', paint)

Label(root, text='move and press the mouse to draw the picture!').pack(side = BOTTOM)

button(root, text = 'delete all', command = (lambda x = ALL: w.delete(x)), bg = 'lightblue').pack(pady = 10, side = BOTTOM)

mainloop()