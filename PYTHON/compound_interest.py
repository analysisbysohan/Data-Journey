# Taking user inputs with float for decimal flexibility
p = float(input("Principal amount: "))
r = float(input("Rate of interest (%): "))
t = float(input("Time in years: "))

# Compound Interest Formula
Amt = p * (pow((1 + r / 100), t))
CI = Amt - p

# Displaying the result rounded to 2 decimal places
print(f"Compound interest: {CI:.2f}")
