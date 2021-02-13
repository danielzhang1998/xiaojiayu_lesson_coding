import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('250x250')

def yes_or_no_check(yes_or_no):
    print(yes_or_no)
    if yes_or_no == 'yes' or yes_or_no == True:
        print('you pick yes')
    elif yes_or_no == 'no' or yes_or_no  == False:
        print('you pick no')

def hit_me1():
    tk.messagebox.showinfo(title='Hi', message='hahaha')

def hit_me2():
    tk.messagebox.showwarning(title='Hi', message='nonono')

def hit_me3():
    tk.messagebox.showerror(title='Hi', message='there is an error!')

def hit_me4():
    yes_or_no = tk.messagebox.askquestion(title='Hi', message='hahaha') # return 'yes' or 'no'
    yes_or_no_check(yes_or_no)

def hit_me5():
    yes_or_no = tk.messagebox.askyesno(title='Hi', message='hahaha') # return True or False
    yes_or_no_check(yes_or_no)

def hit_me6():
    yes_or_no = tk.messagebox.askretrycancel(title='Hi', message='hahaha') # return True or False
    yes_or_no_check(yes_or_no)

def hit_me7():
    yes_or_no = tk.messagebox.askokcancel(title='Hi', message='hahaha') # return True or False
    yes_or_no_check(yes_or_no)

b1 = tk.Button(window, text = 'showinfo', command = hit_me1, width = 15)
b1.pack(pady = 5)

b2 = tk.Button(window, text = 'showwarning', command = hit_me2, width = 15)
b2.pack(pady = 5)

b3 = tk.Button(window, text = 'showerror', command = hit_me3, width = 15)
b3.pack(pady = 5)

b4 = tk.Button(window, text = 'askquestion', command = hit_me4, width = 15)
b4.pack(pady = 5)

b5 = tk.Button(window, text = 'askyesno', command = hit_me5, width = 15)
b5.pack(pady = 5)

b6 = tk.Button(window, text = 'askretrycancel', command = hit_me6, width = 15)
b6.pack(pady = 5)

b7 = tk.Button(window, text = 'askokcancel', command = hit_me7, width = 15)
b7.pack(pady = 5)

window.mainloop()