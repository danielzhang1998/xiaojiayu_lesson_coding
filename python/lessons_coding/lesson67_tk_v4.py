from tkinter import *

root = Tk()

group = LabelFrame(root, text = '最好的脚本语言是：', padx = 5, pady = 5)
group.pack(padx = 10, pady = 10)

LANGS = [
    ('Python', 1),
    ('Java', 2),
    ('C', 3),
    ('R', 4),
    ('MySQL', 5)
]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(group, text = lang, variable = v, value = num, indicatoron = False)
    b.pack(anchor = 'w', fill = X)

mainloop()

#print(v.get())    # get the value