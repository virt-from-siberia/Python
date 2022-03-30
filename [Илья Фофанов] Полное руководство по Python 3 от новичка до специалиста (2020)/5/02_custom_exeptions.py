import math


def calc_square(ab, ac, bc):
    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return s


square = calc_square(10, 10, 10)
print(square)

square = calc_square(-2, 10, 10)
print(square)


def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise ValueError('One of the sides is less or equal to 0.')

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return s


square = calc_square(-2, 10, 10)
print(square)


class InvalidTriangle(Exception):
    """
    Raised when a triangle has invalid sides
    """


def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise InvalidTriangle('One of the sides is less or equal to 0.')

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    return s


try:
    square = calc_square(-2, 10, 10)
except InvalidTriangle as ex:
    print(ex)
else:
    print(square)
