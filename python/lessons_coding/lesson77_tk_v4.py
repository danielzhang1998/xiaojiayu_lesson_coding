from tkinter import *
from PIL import ImageTk as Image_post

root = Tk()

photo = Image_post.PhotoImage(file = '/Users/zhanghanlin/Documents/program/python/小甲鱼/lessons_coding/timg.jpg')


Label(root, text = 'User name').grid(row = 0, padx = 5, pady = 5, sticky = W)
Entry(root).grid(row = 0, column = 1, padx = 5, pady = 5)

Label(root, text = 'Password').grid(row = 1, padx = 5, pady = 5, sticky = W)
Entry(root, show = '*').grid(row = 1, column = 1, padx = 5, pady = 5)

Label(root, image = photo).grid(row = 0, column = 2, rowspan = 2, padx = 5, pady = 5)

Button(text = 'Submit', width = 10, command = lambda x = 'Hello world!': print (x)).grid(row = 2, columnspan = 3, padx = 5, pady = 5)

root.mainloop()