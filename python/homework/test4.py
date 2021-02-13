temp = input("enter a number!\n")
count = int(temp)
while count > 0:
    space = count - 1
    while space > 0:
        print(' ',end='')
        space -= 1
    star = count
    while star > 0:
        print('*',end='')
        star -= 1
    print('\n')
    count -= 1