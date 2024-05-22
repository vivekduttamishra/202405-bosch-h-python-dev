
def read_string(prompt):
    return input(prompt)

def read_int(prompt):
    return int(input(prompt))

def read_float(prompt):
    return float(input(prompt))

def read_bool(prompt):
    value = input(prompt)
    if value.lower() in ("true","t","y","yes","ok"):
        return True
    elif value.lower() in ("false","f","n","no","0",""):
        return False
    else:
        return None
