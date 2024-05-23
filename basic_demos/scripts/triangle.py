

class Triangle:
    pass

def validate(t):
    return t.s1>0 and t.s2>0 and t.s3>0 and \
            t.s1+t.s2>t.s3 and t.s2+t.s3>t.s1 and t.s1+t.s3>t.s2

def perimeter(t):
    if validate(t):
        return t.s1+t.s2+t.s3
    else:
        return None
    
def area(t):
    if validate(t):
        s=(t.s1+t.s2+t.s3)/2
        return (s*(s-t.s1)*(s-t.s2)*(s-t.s3))**0.5
    else:
        return None
    
def draw(t):
    if validate(t):
        print(f'Triangle<{t.s1},{t.s2},{t.s3}>')
    else:
        print("Invalid Triangle")


def create(s1,s2,s3):
    t=Triangle()
    t.s1=s1
    t.s2=s2
    t.s3=s3
    return t


