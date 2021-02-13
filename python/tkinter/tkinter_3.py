import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()

l = tk.Label(window, bg = 'yellow', width = 4, textvariable = var1)
l.pack()

def print_selection():
    value = list_box.get(list_box.curselection())
    var1.set(value)

b1 = tk.Button(window, text = 'print selection', width = 15, height = 2, command = print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44, 'one', 'two', 'three'))

list_box = tk.Listbox(window, listvariable = var2)


list_item = [1, 2, 3, 4]
for item in list_item:
    list_box.insert('end', item)

list_box.insert(1, 'first')

list_box.insert(2, 'second')
list_box.delete(2)

list_box.pack(padx = 10, pady = 10)

window.mainloop()