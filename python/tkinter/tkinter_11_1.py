import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

for i in range(4):
    for j in range(3):
        tk.Label(window, text = 1).grid(row = i, column = j, padx = 10, pady = 10)  # 此处的 padx pady 表示的是修改每一个单元格之间的间距;可使用 ipadx ipady 代替 padx pady

window.mainloop()