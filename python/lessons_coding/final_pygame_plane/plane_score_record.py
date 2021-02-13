import pickle, os
import easygui as g

array = []
ARRAY_LENGTH = 5

# make a new binary file to store the data in list scores
def add_data_set(score):
    global array
    if 'plane_score.testing' not in os.listdir('.'):
         array = []
    else:
        array = data_set_read()
    # auto create a new file if it not exists, or write into the file directly if the file exists
    pickle_file = open('plane_score.testing','wb')   # wb is write binary, do not mind the file name, it can be anything
    for each in score:
        if len(array) < ARRAY_LENGTH:
            array.append(each)
        elif each > array[-1]:
            array[-1] = each
    array = list(reversed(sorted(array)))
    pickle.dump(array, pickle_file)    # dump the list into the file
    pickle_file.close()
    data_set_read()

def data_set_read():
    pickle_file = open('plane_score.testing','rb')   # rb is read binary
    my_list2 = pickle.load(pickle_file) # load the binary data
    return my_list2

if __name__ == '__main__':
    '''    add_data_set(my_time)'''
    enter = input('enter the number:\n')
    if enter.isdigit():
        new_list = []
        enter = int(enter)
        new_list.append(enter)
        add_data_set(new_list)