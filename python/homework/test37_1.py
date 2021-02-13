class Ticket():
    def __init__(self, weekend = False, Child = False):
        self.price = 100
        self.increase = 1
        self.discount = 1
        if weekend:
            self.price = 1.2
        if Child:
            self.discount = 0.5

    def calculate_price(self, num):
        return self.price * self.increase * self.discount * num

adult = Ticket()
child = Ticket(Child = True)

print(adult.calculate_price(2) + child.calculate_price(1))