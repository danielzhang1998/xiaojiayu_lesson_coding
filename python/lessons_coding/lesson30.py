f = open(r'/Users/zhanghanlin/Desktop/chat.txt','r')

A1 = []
B1 = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        array = list(each_line.split(':'))
        if array[0] == 'A':
            A1.append(array[1])
        if array[0] == 'B':
            B1.append(array[1])
    else:
        file_name_A = 'A_' + str(count) + '.txt'
        file_name_B = 'B_' + str(count) + '.txt'

        A_file = open(r'/Users/zhanghanlin/Desktop/text_trying/' + file_name_A,'a')
        B_file = open(r'/Users/zhanghanlin/Desktop/text_trying/' + file_name_B,'a')

        A_file.writelines(A1)
        B_file.writelines(B1)

        A_file.close()
        B_file.close()

        A1 = []
        B1 = []
        count += 1

f.close()

