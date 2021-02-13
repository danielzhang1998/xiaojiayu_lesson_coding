from tkinter import *
from PIL import ImageTk as Image_post

root = Tk()

photo = Image_post.PhotoImage(file = '/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')
Label(root, image = photo).pack()

Button(root, text = 'Click me!', command = lambda x = 'Hello world': print(x)).place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()