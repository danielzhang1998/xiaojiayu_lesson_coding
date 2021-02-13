import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg = 'yellow', width = 20, text = 'empty')
l.pack()

def print_selection():
    if var1.get() and var2.get():
        l.config(text = 'I love both')
    elif var1.get():
        l.config(text = 'I love python')
    elif var2.get():
        l.config(text = 'I love C')
    else:
        l.config(text = 'I do not love either!')

var1 = tk.IntVar()
var2 = tk.IntVar()

# 此处需要设置 checkbutton 的 width，否则会出现不对齐的问题
check_button1 = tk.Checkbutton(window, text = 'Python', variable = var1, onvalue = 1, offvalue = 0, command = print_selection, width = 10)
check_button2 = tk.Checkbutton(window, text = 'C', variable = var2, onvalue = 1, offvalue = 0, command = print_selection, width = 10)
check_button1.pack()
check_button2.pack()

window.mainloop()