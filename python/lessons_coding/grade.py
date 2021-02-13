while True:
    temp = input("please enter your mark!\n")
    level = "UNDEFINED"
    if temp.isdigit():
        if 90 <= int(temp) <= 100:
            level = "A"
            break
        elif 80 <= int(temp) < 90:
            level = "B"
            break
        elif 60 <= int(temp) < 80:
            level = "C"
            break
        elif 0 <= int(temp) < 60:
            level = "D";
            break
    else:
        print("error insert, please try again!")
print("your mark is: " + str(temp) + ", it is level " + level)
