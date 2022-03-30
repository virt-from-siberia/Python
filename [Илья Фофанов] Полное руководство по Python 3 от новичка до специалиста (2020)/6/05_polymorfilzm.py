import math


class Shape():

    def __init__(self):
        print('Shape created')

    def draw(self):
        print('Drawing a shape')
        raise NotADirectoryError('Can not instantiate')

    def aria(self):
        print('Calc aria')
        raise NotADirectoryError('Can not instantiate')

    def perimeter(self):
        print('Calc perimeter')
        raise NotADirectoryError('Can not instantiate')


shape = Shape()


class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)

        self.width = width
        self.height = height

        print('Rectangle created')

        Shape.aria(self)

    def aria(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f"Drawing rectangle with width={self.width} and height={self.height}")


react = Rectangle(10, 15)
print(react.aria())
print(react.draw())


class Triangle(Shape):

    def __init__(self, a, b, c):
        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print('Triangle created')

    def draw(self):
        print(f'Drawing triangle with side={self.a}, {self.b}, {self.c}')

    def aria(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle(10, 10, 10)
print(triangle.draw())
print(triangle.aria())
print(triangle.perimeter())

for shape in [react, triangle]:
    shape.draw()
