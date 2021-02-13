import easygui as g
import os

file_path = g.fileopenbox(default = '*.txt')

with open(file_path) as old_f:
    title = os.path.basename(file_path)
    msg = ''
    text = old_f.read()
    new_f = g.textbox(msg, title, text)

if text != new_f[:]:
    choice = g.choicebox('the data has been changed','alert',('Save', 'Cancel', 'Save As'))
    if choice == 'Save':
        with open(file_path, 'w') as old_f:
            old_f.write(new_f[:])
    if choice == 'Save As':
        new_path = g.filesavebox(default = '.txt')
        if os.path.splitext(new_path)[1] != '.txt':
            new_path += '.txt'
        with open(new_path, 'w') as new:
            new.write(new_f[:])