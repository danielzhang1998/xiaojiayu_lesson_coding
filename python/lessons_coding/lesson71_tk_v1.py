from tkinter import *

root = Tk()

text = Text(root, width = 30, height = 5)
text.pack()

text.insert(INSERT, 'I love FishC.com!')
text.tag_add('tag1','1.13','1.16')    # 设置tag
text.tag_add('tag2','1.11')    # 设置tag
text.tag_config('tag1', background = 'yellow', foreground = 'red')  # 对标签的样式进行设置
text.tag_config('tag2', background = 'gray', foreground = 'white')  # 对标签的样式进行设置

mainloop()