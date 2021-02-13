from tkinter import *

root = Tk()

def create():
    top = Toplevel()
    top.attributes('-alpha', 0.75)
    top.title('FishC Demo')

    msg = Message(top, text = 'I love FishC.com!')
    msg.pack()

b1 = Button(root, text = 'Make the most top window', command = create)
b1.pack()

root.mainloop()