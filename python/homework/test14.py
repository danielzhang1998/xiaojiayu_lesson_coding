password = input("please enter your password here!\n")
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

# check the length of the password
def length(password):
    if 8 < len(password) < 16:
        return 1
    elif len(password) >= 16:
        return 2
    elif len(password) == 0:
        return -1
    else:
        return 0

# check the components
def components(password):
    sum_all = 0
    for each in password:
        if each in symbols:
            sum_all += 1
            break
    for each in password:
        if each in chars:
            sum_all += 1
            break
    
    for each in password:
        if each in nums:
            sum_all += 1
            break
    return sum_all       

# check the password start with character
def start_by_word(password):
    if password[0] in chars:
        return 1
    else:
        return 0       

if length(password) == 0 or components(password) == 1:
    print("low level")
elif components(password) == 3 and start_by_word(password) == 1 and length(password) == 2:
    print("high level")
elif length(password) == -1:
    print("you enter nothing, please try again!")
else:
    print("middle level")