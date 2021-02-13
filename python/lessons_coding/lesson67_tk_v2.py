from tkinter import *

root = Tk()

GIRLS = ['xiaojiayu1','xiaojiayu2','xiaojiayu3','xiaojiayu4','xiaojiayu5']

v = []

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text = girl, variable = v[-1])
    b.pack(anchor = 'w')

mainloop()