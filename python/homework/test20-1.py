f = open(r'/Users/zhanghanlin/Documents/program/python/小甲鱼/homework/string1.txt', 'r')
list1 = []
for each_line in f:
    for each_word in each_line:
        if each_word not in list1:
            list1.append(each_word)

print(list1)