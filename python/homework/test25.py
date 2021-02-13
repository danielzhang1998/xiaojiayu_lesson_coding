print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

details = dict()

details['Tom'] = 123456

while True:
    enter = input('please enter the code you want to execute:\n')
    enter = int(enter)

    if enter == 1:
        name = input('please enter the name you want to check:\n')
        phone_num = details.get(name)
        if phone_num != None:
            print(name + '\'s number is: ' + str(phone_num))
        else:
            print(name + ' is not exists!')

    elif enter == 2:
        name = input('please enter the name you want to insert:\n')
        phone_num = details.get(name)
        if phone_num != None:
            print(name + ' is exists!')
            print(name + '\'s number is: ' + str(phone_num))
            check = input('are you sure to modify? please enter y/n\n')
            if check == 'y':
                details[name] = input('please enter the new phone number here:\n')
        else:
            details[name] = input('please enter the new phone number here:\n')

    elif enter == 3:
        name = input('please enter the name you want to delete:\n')
        phone_num = details.get(name)
        if phone_num == None:
            print('the people try do delete is not exists!')
        else:
            del(details[name])

    elif enter == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')