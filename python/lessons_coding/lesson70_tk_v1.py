from tkinter import *
from PIL import ImageTk as Image_post

root = Tk()

new_text = Text(root, width = 100, height = 100)
new_text.pack()

new_text.insert(INSERT, 'I love ')
new_text.insert(END, 'FishC.com\n')

photo = Image_post.PhotoImage(file = '/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/cat_600_800.jpg')

def show():
    new_text.image_create(END, image = photo)

b1 = Button(new_text, text = 'Click me!', command = show)
new_text.window_create(INSERT, window = b1)

mainloop()