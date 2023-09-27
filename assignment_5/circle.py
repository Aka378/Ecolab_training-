from math import pi

class Circle:
    pass

def create(radius):
    c = Circle()
    c.radius = radius
    return c

def is_valid(c):
    return isinstance(c, Circle) and c.radius > 0

def area(c):
    return pi * c.radius ** 2 if is_valid(c) else float('nan')

def perimeter(c):
    return 2 * pi * c.radius if is_valid(c) else float('nan')

def info(c):
    return f'Circle<{c.radius}>' if is_valid(c) else '<Invalid Circle>'

def draw(c):
    print(info(c))

def test_circle(radius):
    c = create(radius)
    draw(c)
    if is_valid(c):
        print(f'Area = {area(c)}')
        print(f'Perimeter = {perimeter(c)}')

test_circle(10)