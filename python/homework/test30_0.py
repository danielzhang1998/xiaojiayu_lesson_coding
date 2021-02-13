import os

array = os.listdir('.')
dict1 = {}

count = 1
dict1['folder'] = 0

for each in array:
    if '.' in each:
        if ('.' + each.split('.')[-1]) not in dict1:
            dict1['.' + str(each.split('.')[-1])] = count
        else:
            new_num = dict1.get('.' + str(each.split('.')[-1]))
            new_num += 1
            dict1['.' + str(each.split('.')[-1])] = new_num
    else:
        dict1['folder'] = dict1.get('folder') + 1
print(dict1)