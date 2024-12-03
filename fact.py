# Program to calculate the factorial of a predefined number

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Predefined number
num = 5

# Calculate and display the factorial
result = factorial(num)
print(f"The factorial of {num} is: {result}")

