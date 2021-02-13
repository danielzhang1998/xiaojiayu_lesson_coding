filename1 = input('please enter the first filename you want to check\n')

filename2 = input('please enter the second filename you want to check\n')

LOCATION = '/Users/zhanghanlin/Documents/program/python/'

filename1 = LOCATION + filename1
filename2 = LOCATION + filename2

f1 = open(filename1, 'r')
f2 = open(filename2, 'r')

count = 0

array1 = []
array2 = []

for each in f1:
    array1.append(each)

for each in f2:
    array2.append(each)

if len(array1) >= len(array2):
    for each in range(len(array2)):
        if array2[each] != array1[each]:
            count += 1
else:
    for each in range(len(array1)):
        if array1[each] != array2[each]:
            count += 1

f1.close()
f2.close()
print(count)