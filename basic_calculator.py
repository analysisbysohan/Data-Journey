# calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: b = zero is not allowed"
    return a / b

def floor_div(a, b):
    if b == 0:
        return "Error: b = zero is not allowed"
    return a // b
