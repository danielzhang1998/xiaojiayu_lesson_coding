filename1 = input('please enter the second filename you want to print\n')

LOCATION = '/Users/zhanghanlin/Documents/program/python/'

filename1 = LOCATION + filename1

enter = input('how many rows need to print?\n')

enter = int(enter)

f = open(filename1, 'r')

count = 1

for each in f:
    if count <= enter:
        print(each)
        count += 1

f.close()