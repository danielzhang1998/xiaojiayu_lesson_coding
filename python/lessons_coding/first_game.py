import random
import easygui as g

print("---------- This is my first try -----------")
number = random.randint(0, 19)   # get a random number from [0,19]
times = 0   # how many chance the player already used
chance = 5  # how many chance the player have
#number = str(number)
while(times < chance):
    temp = g.enterbox(msg='', title='terminal', strip=True, image=None, root=None)
    if temp.isdigit():
        times += 1
        #guess = str(temp)
        guess = int(temp)
        if(guess == number):
            g.msgbox("yes, you are right!\nCongradulations, you win!")
            break
        else:
            if(times < chance):
                g.msgbox("please try again!")
                if(guess < number):
                    g.msgbox("it is too small!")
                elif(guess > number):
                    g.msgbox("it is too big!")
                g.msgbox("chance tried: " + str(times) + "/" + str(chance))
            else:
                g.msgbox("you run out of the chance!\ngame is over!")
    else:
        continue