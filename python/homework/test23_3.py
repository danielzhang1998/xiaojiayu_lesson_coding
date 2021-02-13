year = 10

def age(number):
    global age
    if number == 1:
        return year
    else:
        return age(number - 1) + 2

print(age(5))