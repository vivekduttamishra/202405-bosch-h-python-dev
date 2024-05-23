import math

class Circle:
    pass

def validate(c):
    return isinstance(c,Circle) and c.r>0

def perimeter(c):
    if validate(c):
        return 2*math.pi*c.r
    else:
        return None
    
def area(c):
    if validate(c):
        return math.pi*c.r**2
    else:
        return None
    
def create(radius):
    c=Circle()
    c.r=radius
    return c

def draw(c):
    if validate(c):
        print(f'Circle({c.r})')
    else:
        print("Invalid Circle")


