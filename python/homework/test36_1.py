class Rectangle:
    height = 5
    width = 4

    def set_height_width(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_Rect(self):
        print('the rect is: ' + str(self.width) + ', ' + str(self.height))

    def get_Area(self):
        print('the area is: ' + str(self.width * self.height))

rec1 = Rectangle()
rec1.set_height_width(10, 5)
rec1.get_Rect()
rec1.get_Area()