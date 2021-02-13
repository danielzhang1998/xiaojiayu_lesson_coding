import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg = 'yellow', width = 20, text = 'empty')
l.pack()

'''
var = tk.StringVar()
'''

# 注意此处需要写入值 v
def print_selection(v):
    l.config(text = 'you have selected ' + v)

# from_ 表示其实位置
# to 表示末尾位置
# orient 表示刻度轴是横向还是纵向
# length 表示刻度轴的长度，单位是 px
# showvalue 1 是 显示当前值， 0 是不显示
# tickinterval 表示刻度
# resolution 表示保留几位小数，如果为 1 则只保留整数
s = tk.Scale(window, label = 'try me', from_ = 5, to = 11, orient = tk.HORIZONTAL, length = 200, showvalue = 1, tickinterval = 3, resolution = 0.01, command = print_selection)
s.pack()

window.mainloop()