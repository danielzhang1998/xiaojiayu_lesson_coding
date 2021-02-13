import tkinter as tk
from PIL import ImageTk as Image_post

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

move_int = 2

def moveit():
    global move_int
    if (int(canvas.coords(rect)[3]) == int(canvas.winfo_height()) - 6) or (int(canvas.coords(rect)[1]) == 6):   # 触碰边界弹回
        move_int = - move_int
    canvas.move(rect, 0, move_int) # 横向移动 0， 纵向移动 2
    #print(canvas.coords(rect)) # 获取正方形的坐标位置

canvas = tk.Canvas(window, bg = 'lightblue', height = 100, width = 200)
canvas.pack()

photo_file = Image_post.PhotoImage(file = '/Users/zhanghanlin/Documents/program/python/tkinter/cat_600_800.jpg')
image = canvas.create_image(0, 0, anchor = 'nw', image = photo_file)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1, fill = 'white')
oval = canvas.create_oval(x0, y0, x1, y1, fill = 'pink')
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start = 0, extent = 180, fill='gold')   # start 是从什么度数开始，extent 是在什么度数结束
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20, fill = 'lightgrey')

b = tk.Button(window, text = 'move', command = moveit).pack()

window.mainloop()