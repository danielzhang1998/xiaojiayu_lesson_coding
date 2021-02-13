from tkinter import *

root = Tk()

w1 = Message(root, text = 'This is a message', width = 200)
w1.pack()

w2 = Message(root, text = 'This is a really really long message', width = 200)
w2.pack()

root.mainloop()