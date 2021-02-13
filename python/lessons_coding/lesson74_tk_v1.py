from tkinter import *


def doNothing():
    label1 = Label(root, text="Doing nothing")
    label1.pack()

root = Tk()


mainmenu = Menu(root)
root.config(menu=mainmenu)


filemenu = Menu(mainmenu)
mainmenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Project", command=doNothing)
filemenu.add_command(label="New", command=doNothing)


Submenu = Menu(mainmenu)
filemenu.add_cascade(label="Open", menu = Submenu)
Submenu.add_command(label = 'From local')
Submenu.add_command(label = 'From web')
Submenu.add_command(label = 'From OneDrive')
Submenu.add_command(label = 'From GitHub')
Submenu.add_command(label = 'Other')


filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

editmenu=Menu(mainmenu)

mainmenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo", command=doNothing)

root.mainloop()