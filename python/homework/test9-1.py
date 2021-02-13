passwd = 'password'
chance = 3
while chance > 0:
    temp = input("please enter your password!\n")
    str1 = str(temp)
    if "*" in str1:
        print("the password can not include '*', please try again! Chance left: " + str(chance - 1), end = '.  ')
    elif str1 != passwd:       
        print("the password insert is wrong, please try again! Chance left: " + str(chance - 1), end = '.  ')     
        chance -= 1   
    else:
        print("log in sussessful!")
        break
