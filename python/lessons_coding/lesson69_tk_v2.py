from tkinter import *

master = Tk()

animals = ['pig','tiger','elephant','dog','cat','snake','cow','lion','bird','dragon', 'ant', 'etc.']

theLB = Listbox(master, selectmode = MULTIPLE, height = len(animals))  # 多选 ; 选项显示的个数
theLB.pack(padx = 10, pady = 10)

for each in range(len(animals)):
    theLB.insert(each, animals[each])

mainloop()