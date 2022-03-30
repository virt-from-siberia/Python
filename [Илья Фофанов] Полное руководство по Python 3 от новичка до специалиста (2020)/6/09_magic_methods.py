class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"point x={self.x} y={self.y}"


point = Point(4, 5)
print(point)


class Road():
    def __init__(self, length):
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f"a road length={self.length}"

    def __del__(self):
        print(f"the road has been destroyed")


road = Road(100)
len(road)
del(road)
