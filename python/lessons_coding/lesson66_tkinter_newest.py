from tkinter import *
from tkmacosx import Button as button
from PIL import ImageTk as Image_post

def callback():
    var.set('I don\'t believe it!')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('This is a cat picture !')

textLabel = Label(root, textvariable = var,justify=LEFT)
textLabel.pack(side=LEFT)

photo = Image_post.PhotoImage(file='/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')
imageLabel = Label(frame1, image = photo)
imageLabel.pack(side=RIGHT)

theBUtton = button(frame2, text = 'I know it!', command = callback)
theBUtton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()
