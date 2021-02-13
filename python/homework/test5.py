while True:
    temp = input("please enter the correct year number to run the program!\n")
    if temp.isdigit():
        break
year = int(temp)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(temp + " is a leap year!")
else:
    print(temp + " is not a leap year!")