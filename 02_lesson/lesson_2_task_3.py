import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = 4.5
square_area = square(side_length)

print(f"Площадь квадрата со стороной {side_length}: {square_area}")
