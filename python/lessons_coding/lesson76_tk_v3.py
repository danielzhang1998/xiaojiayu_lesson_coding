from tkinter import *

root = Tk()

m = PanedWindow(orient = VERTICAL)
m.pack(fill = BOTH, expand = 1)

top = Label(m, text = 'top pane')
m.add(top)

bottom = Label(m, text = 'bottom pane')
m.add(bottom)

root.mainloop()