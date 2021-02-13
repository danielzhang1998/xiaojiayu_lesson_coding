import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self):
        self.power = 100
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        position_x = self.x + r.choice([1,2,-1,-2])
        position_y = self.y + r.choice([1,2,-1,-2])

        if position_x < legal_x[0]:
            self.x = legal_x[1] + position_x
        elif position_x > legal_x[1]:
            self.x = position_x - legal_x[1]
        else:
            self.x = position_x

        if position_y < legal_y[0]:
            self.y = legal_y[1] + position_y
        elif position_y > legal_y[1]:
            self.y = position_y - legal_y[1]
        else:
            self.y = position_y        

        self.power -= 1
        return(self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        position_x = self.x + r.choice([1,-1])
        position_y = self.y + r.choice([1,-1])

        if position_x < legal_x[0]:
            self.x = legal_x[1] + position_x
        elif position_x > legal_x[1]:
            self.x = position_x - legal_x[1]
        else:
            self.x = position_x

        if position_y < legal_y[0]:
            self.y = legal_y[1] + position_y
        elif position_y > legal_y[1]:
            self.y = position_y - legal_y[1]
        else:
            self.y = position_y        

        return(self.x, self.y)

turtle = Turtle()
fish = []
for each in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('the pool has no more fish, thanks for playing!')
        break
    if not turtle.power:
        print('the turtle has no more power, game is over!')
        break

    pos = turtle.move()

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print('one fish has been eaten, the fish left: ' + str(len(fish)))