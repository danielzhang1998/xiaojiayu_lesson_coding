import tkinter as tk
import os
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('Welcome to my window')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height = 200, width = 500)
image_file = tk.PhotoImage(file = os.getcwd() + '/python/tkinter/log_in' + '/welcome.gif')
image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
canvas.pack(side = 'top')

# user information
tk.Label(window, text = 'User name:').place(x = 50, y = 150)
tk.Label(window, text = 'Password:').place(x = 50, y = 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable = var_usr_name)
entry_usr_name.place(x = 160, y = 150)

var_usr_pwd = tk.StringVar()
entry_pwd = tk.Entry(window, textvariable = var_usr_pwd, show = '*')
entry_pwd.place(x = 160, y = 190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(title = 'Welcome', message = 'How are you today? ' + usr_name)
        else:
            messagebox.showerror(title = 'Error', message =  'Your password is wrong!')
    else:
        is_sign_up = tk.messagebox.askyesno(title = 'Welcome', message = 'You have not sign up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():

    def sign():
        np = new_pwd.get()
        npc = new_pwd_confirm.get()
        nn = new_name.get()
        try:
            with open('usrs_info.pickle', 'rb+') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb+') as usr_file:
                usrs_info = {'admin':'admin'}
                pickle.dump(usrs_info, usr_file)

        if np == npc:
            if nn not in usrs_info:
                with open('usrs_info.pickle', 'wb') as usr_file:
                    usrs_info[nn] = np
                    pickle.dump(usrs_info, usr_file)
                    messagebox.showinfo(title = 'Welcome', message = 'You have successfully signed up!')
                    window_sign_up.destroy()
            else:
                messagebox.showwarning(title = 'Warning', message = 'The user name already exists!')
        else:
            messagebox.showwarning(title = 'Warning', message = 'Please check the password, it is different with the confirm password!')        

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set(var_usr_name.get())
    tk.Label(window_sign_up, text = 'User name:').place(x = 10, y = 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable = new_name)
    entry_new_name.place(x = 150, y = 10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text = 'Password:').place(x = 10, y = 50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable = new_pwd, show = '*')
    entry_usr_pwd.place(x = 150, y = 50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text = 'Confirm password:').place(x = 10, y = 90)
    new_pwd_confirm = tk.Entry(window_sign_up, textvariable = new_pwd_confirm, show = '*')
    new_pwd_confirm.place(x = 150, y = 90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text = 'Sign up', command = sign)
    btn_confirm_sign_up.place(x = 150, y = 130)

# login and sign up button
btn_login = tk.Button(window, text = 'Login', command = usr_login)
btn_login.place(x = 170, y = 230)
btn_sign_up = tk.Button(window, text = 'Sign up', command = usr_sign_up)
btn_sign_up.place(x = 270, y = 230)

window.mainloop()