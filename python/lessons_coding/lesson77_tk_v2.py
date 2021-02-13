from tkinter import *

root = Tk()

Label(root, text = 'black', bg = 'lightgray', fg = 'black', width = 50).pack(fill = X)
Label(root, text = 'blue', bg = 'yellow', fg = 'blue', width = 50).pack(fill = X)
Label(root, text = 'red', bg = 'white', fg = 'red', width = 50).pack(fill = X)

Label(root, text = 'black', bg = 'lightgray', fg = 'black', width = 50).pack(side = LEFT)
Label(root, text = 'blue', bg = 'yellow', fg = 'blue', width = 50).pack(side = LEFT)
Label(root, text = 'red', bg = 'white', fg = 'red', width = 50).pack(side = LEFT)

root.mainloop()