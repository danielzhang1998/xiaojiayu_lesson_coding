# find the prime number

def find(number):
    num1 = number // 2  # the smallest multiple is 2
    while 1 < num1 <= number:
        if number %num1 == 0:
            print('the biggest divisor for ' + str(number) + ' is: ' + str(num1))
            break
        num1 -= 1
    else:
        print(str(number) + ' is a prime number')

number = int(input('please enter a number: \n'))
find(number)
