import translate_browser_enter
import easygui as gui

def change_format(string1):
    enter = gui.enterbox(msg='enter the things that you want to translate here! or enter q! to quit!', title='Translate', default='', strip=True, image=None, root=None)
    if enter == 'q!':
        return -1
    data_set = {}
    list1 = string1.splitlines()
    for each in list1:
        if each != '':
            string2 = ''
            string2 = each
            list2 = string2.split(': ')
            if list2[0] != 'i':
                data_set[list2[0]] = list2[1] 
            else:
                data_set[list2[0]] = enter
    return data_set

if __name__ == '__main__':
    new_dict = change_format(translate_browser_enter.string1)
    print(new_dict)



