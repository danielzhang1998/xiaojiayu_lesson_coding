filename = input('please enter the filename you want to create\n')

LOCATION = '/Users/zhanghanlin/Documents/program/python/'

filename = LOCATION + filename

array = []

while True:
    content = input('please enter the contents want to write:\n')
    if content == ':w':
        break
    else:
        array.append(content)

try:
    f = open(filename, 'w')
    for each in array:
        f.write(each + '\n')
    f.close()
except OSError as e:
    print(e)