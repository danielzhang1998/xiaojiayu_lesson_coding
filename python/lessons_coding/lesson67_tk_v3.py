from tkinter import *

root = Tk()

v = IntVar()

One = Radiobutton(root, text = 'One', variable = v,value = 1).pack(anchor = 'w')
Two = Radiobutton(root, text = 'Two', variable = v,value = 2).pack(anchor = 'w')
Three = Radiobutton(root, text = 'Three', variable = v,value = 3).pack(anchor = 'w')

mainloop()

# print(v.get())    # get the value