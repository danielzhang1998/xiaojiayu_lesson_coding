from tkinter import *

master = Tk()

sb = Scrollbar(master)
sb.pack(side = RIGHT, fill = Y)

theLB = Listbox(master, yscrollcommand = sb.set)

for each in range(1000):
    theLB.insert(END, each)

theLB.pack(side = LEFT, fill = BOTH)

sb.config(command = theLB.yview)

mainloop()