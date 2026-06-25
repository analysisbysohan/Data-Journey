# Function to calculate Simple Interest
def calculate_simple_interest(p, t, r):
    return (p * t * r) / 100

# Taking user inputs and converting them to floats for decimal flexibility
principal = float(input("Enter the Principal amount: "))
time = float(input("Enter the Time period (in years): "))
rate = float(input("Enter the Rate of interest (%): "))

# Calculating result
interest = calculate_simple_interest(principal, time, rate)

# Displaying a clean, human-readable result
print(f"\nCalculated Simple Interest: {interest}")
