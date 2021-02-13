from tkinter import *

root = Tk()

Label(root, text = 'Account: ').grid(row = 0, column = 0)
Label(root, text = 'Password: ').grid(row = 1, column = 0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root, textvariable = v1)
e2 = Entry(root, textvariable = v2, show = '*') # 作为 星号 显示
e1.grid(row = 0, column = 1, padx = 10, pady = 5)
e2.grid(row = 1, column = 1, padx = 10, pady = 5)

def show():
    print('Account: ' + e1.get())
    print('Password: ' + e2.get())
    e1.delete(0, END)
    e2.delete(0, END)

Button(root, text = 'Log in', width = 20, command = show).grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
Button(root, text = 'Exit', width = 10, command = root.quit).grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)

mainloop()