import copy

list1 = [1, 2, 3, [4, 5, 6]]

copied_list = list1.copy()
copied_list[3].append(7)
copied_list[2] = 7

print(list1)
print(copied_list)

list1.append(8)

print(list1)
print(copied_list)

shallow_copy = copy.copy(list1)
shallow_copy[3].append(8)

print(list1)
print(shallow_copy)

deep_copy = copy.deepcopy(list1)
deep_copy[3].append(0)

print(list1)
print(deep_copy)


class Point():

    def __init__(self, x, y):
        self.p1 = x
        self.y = y

    def repr(self):
        return f"Point {self.x} , {self.y}"


a = Point(1, 2)
b = copy.copy(a)
a.x = 3

print(a)
print(b)


class Line():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result

        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))

        return result


l1 = Line(a, b)
l2 = copy.copy(l1)

print("=====")
print(l1)
print(l2)

l1.p1.x = 4

print(l1)
print(l2)

l1 = Line(a, b)
l2 = copy.deepcopy(l1)
