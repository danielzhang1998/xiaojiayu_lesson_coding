import tkinter as tk
from tkinter.filedialog import askopenfilename
# 获得所选的文件的地址

path_list = []
name = []

class Files():
    def __init__(self, i):
        self.etyText = tk.StringVar()
        self.name = f'name{i}'

    def btn_action(self):
        position = -1
        sPath = askopenfilename()
        if len(sPath) > 0:
            self.etyText.set(sPath)
        if len(path_list) == 3:
            for each in range(len(name)):
                if str(self.name) in name[each]:
                    del name[each]
                    del path_list[each]
                    position = each
                    break
        if len(path_list) < 3 and position != -1:
            path_list.insert(position, sPath)
            name.insert(position, str(self.name))
        else:
            path_list.append(sPath)
            name.append(str(self.name))

if __name__ == '__main__':
    root = tk.Tk()
    root.title('test')
    root.geometry('500x200+500+200')
    iCount = 3


    for i in range(1, iCount + 1):
        file = Files(i)  # 實例化類
        tk.Label(root, text='lb' + str(i)).grid(row=i, column=0)
        file.name=tk.Entry(root, textvariable=file.etyText, width=40)
        file.name.grid(row=i, column=1)
        tk.Button(root, text='選擇文件', command=file.btn_action).grid(row=i, column=2)

    def show_path():
        print(path_list)

    tk.Button(root, text='Run', command=show_path).grid(row=iCount + 1, column=1)

    tk.mainloop()
