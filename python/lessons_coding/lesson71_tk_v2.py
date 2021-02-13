from tkinter import *
import webbrowser as web

root = Tk()

new_text = Text(root, width = 30, height = 10)
new_text.pack()

new_text.insert(INSERT, 'I love FishC.com!')

new_text.tag_add('link','1.7','1.16')
new_text.tag_config('link', foreground = 'blue', underline = True)

def show_hand_cursor(event):
    new_text.config(cursor = 'arrow')

def show_xterm_cursor(event):
    new_text.config(cursor = 'xterm')

def click(event):
    web.open('http://www.fishc.com')

new_text.tag_bind('link', '<Enter>', show_hand_cursor)
new_text.tag_bind('link', '<Leave>', show_xterm_cursor)
new_text.tag_bind('link', '<Button-1>', click)

mainloop()