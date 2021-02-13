import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()

l = tk.Label(window, bg = 'yellow', width = 15, text = 'empty')
l.pack()

def print_selection():
    l.config(text = 'you have selected ' + var.get())

var.set(0)

radio_button1 = tk.Radiobutton(window, text = 'Option A', variable = var, value = 'A', command = print_selection)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text = 'Option B', variable = var, value = 'B', command = print_selection)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text = 'Option C', variable = var, value = 'C', command = print_selection)
radio_button3.pack()

window.mainloop()