def add(a, b):
    if type(a) is not int and type(a) is not float:
        raise ValueError("A must be an integer")
    elif type(b) is not int and type(b) is not  float:
        raise ValueError("B must be an integer")
    
    return int(a) + int(b)