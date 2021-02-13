import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

count = 0

l = tk.Label(window, text = '', bg = 'yellow')
l.pack()

def do_job():
    global count
    l.config(text = 'do' + str(count))
    count += 1

# 第一个父菜单栏
menubar = tk.Menu(window)
window.config(menu = menubar)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'New', command = do_job)
filemenu.add_command(label = 'Open', command = do_job)
filemenu.add_command(label = 'Save', command = do_job)
filemenu.add_separator()    # 分割线
filemenu.add_command(label = 'Exit', command = window.quit)

# 菜单栏的子菜单栏
Submenu = tk.Menu(menubar)
filemenu.add_cascade(label = 'Import', menu = Submenu)
Submenu.add_command(label = 'testing1', command = do_job)
Submenu.add_command(label = 'testing2', command = do_job)
Submenu.add_command(label = 'testing3', command = do_job)

# 第二个父菜单栏
new_menubar = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = new_menubar)
new_menubar.add_command(label = 'Cut', command = do_job)
new_menubar.add_command(label = 'Copy', command = do_job)
new_menubar.add_command(label = 'Paste', command = do_job)

window.mainloop()