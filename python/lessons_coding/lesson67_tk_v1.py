from tkinter import *

root = Tk()

v = IntVar()

c = Checkbutton(root, text = 'testing', variable = v)
c.pack()

l = Label(root, textvariable = v)   # 查看 button 是否被选中了
l.pack()

mainloop()