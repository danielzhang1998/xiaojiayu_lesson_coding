from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode = MULTIPLE)  # 多选
theLB.pack(padx = 10, pady = 10)

animals = ['pig','tiger','elephant','dog','cat','snake','cow','lion','bird','dragon', 'ant', 'etc.']
for each in range(len(animals)):
    theLB.insert(each, animals[each])

#theLB.delete(0, END)    # delete all
#theLB.delete(1) # delete the 1st one, start from 0, so it will delete 'tiger' from the list

theButton = Button(master, text = 'Delete it', command = lambda x = theLB: x.delete(ACTIVE))

theButton.pack()

mainloop()