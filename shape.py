class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return

    def perimeter(self):
        return


class Circle(Shape):
    def area(self):
        print("pi time ", self.length * self.length)

    def perimeter(self):
        print("2 times pi times ", self.length)


class Square(Shape):
    def area(self):
        print(self.length * self.length)

    def perimeter(self):
        print("4 times ", self.length)


class Triangle(Shape):

    def __init__(self, length, height):
        super().__init__(length)
        self.height = height

    def area(self):
        print(self.height * self.length)

    def perimeter(self):
        print("periphery")