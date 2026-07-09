# calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0 :
        return "Error: b = zero is not allowed"
    return a / b

def floor_div(a, b):
    if b == 0 :
        return "Error: b = zero is not allowed"
    return a // b

def factorial (n):
    if n < 0 :
        return "Error, Negative number is not Allowed"
    if n == 0: 
     return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(n):
    """Calculates the sum of digits using pure math."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10  # Gets the last digit
        n = n // 10      # Removes the last digit
    return total
