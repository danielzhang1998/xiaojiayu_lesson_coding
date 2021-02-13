from tkinter import *

master = Tk()

s1 = Scale(from_=0,to=42, tickinterval = 5, resolution = 5, length = 300)   # tivkinterval 表示刻度, resolution 表示精度, length 表示显示长度
s1.pack()

s2 = Scale(from_=0,to=200, orient = HORIZONTAL, tickinterval = 10, length = 1000)   # HORIZONTAL 表示水平显示，默认为垂直显示
s2.pack()

def get_p():
    print(s1.get(), s2.get())

Button(master, text = 'get the position', command = get_p).pack()

mainloop()