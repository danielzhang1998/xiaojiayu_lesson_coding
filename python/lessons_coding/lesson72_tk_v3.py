from tkinter import *
from tkmacosx import Button as button

root = Tk()

w = Canvas(root, width = 1000, height = 500, background = 'lightgray')
w.pack(padx = 10, pady = 10)

line1 = w.create_line(0, 250, 1000, 250, fill='black', width = 1)

rectangle1 = w.create_rectangle(200, 100, 800, 400, fill='white')
w.create_oval(200, 100, 800, 400, fill = 'pink')

w.create_oval(350, 100, 650, 400, fill = 'gray')

line2 = w.create_line(500, 0, 500, 500, fill='black', dash = (4, 4), width = 5)

w.create_text(500, 250, text = 'I am the center!', fill = 'white', font = ('Arial', 30))



# w.coords(line1, 0, 125, 1000, 125)  # move the item to the new place

# w.itemconfig(rectangle1, fill = 'pink') # change the item color

# w.delete(rectangle1)  # remove the item

button(root, text = 'delete all', command = (lambda x = ALL: w.delete(x)), bg = 'lightblue').pack(pady = 10)

mainloop()