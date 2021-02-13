from tkinter import *
from PIL import ImageTk as Image_post

root = Tk()

photo = Image_post.PhotoImage(file = '/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/cat_600_800.jpg')
theLabel = Label(root,
            text = 'This is another cat picture!',
            justify = LEFT,
            image = photo,
            compound = CENTER,
            font = ('Arial', 20),
            fg = 'white')

theLabel.pack()

mainloop()