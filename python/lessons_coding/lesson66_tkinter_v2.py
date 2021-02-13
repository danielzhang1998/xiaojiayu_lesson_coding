from tkinter import *
from tkmacosx import Button as button
from PIL import ImageTk as Image_post

root = Tk()

textLabel = Label(root, text = 'This is a cat picture !',justify=LEFT,padx=10)
textLabel.pack(side=LEFT)

photo = Image_post.PhotoImage(file='/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')
imageLabel = Label(root, image = photo)
imageLabel.pack(side = RIGHT)

mainloop()
