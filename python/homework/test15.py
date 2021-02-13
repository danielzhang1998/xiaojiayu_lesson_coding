q = True

while q:
    num = input('please enter the number that need to transfer:\n')
    if num.isdigit():
        num = int(num)
        print('十进制 --> 十六进制: ' + '%d' % num +'--> 0x' + '%x' % num)
        print('十进制 --> 八进制: ' + '%d' % num +'--> 0o' + '%o' % num)
        print('十进制 --> 二进制: ' + '%d' % num +'--> ' + bin(num))
    elif num == 'Q':
        q = False
    else:
        continue