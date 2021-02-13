from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx = 20, pady = 20)

e.delete(0, END)    # 删除输入框中的所有文本，从 0 开始， END 结尾
e.insert(0, '默认文本...')  # 在输入框中插入文本，从 0 开始

mainloop()