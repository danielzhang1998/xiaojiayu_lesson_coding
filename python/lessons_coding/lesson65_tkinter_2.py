import tkinter as tk
from tkmacosx import Button as button

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx = 20, pady = 10)
        self.hi_there = button(frame, text='Hello!', bg = 'black', fg = 'white', command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print("Hello everyone, I am a python file!:)")

root = tk.Tk()
app = APP(root)

root.mainloop()