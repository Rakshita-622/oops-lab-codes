def is_disarium(number):
    digits = str(number)
    sum_of_powers = sum(int(digit) ** (i + 1) for i, digit in enumerate(digits))
    return sum_of_powers == number

num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")

def is_harshad(number):
    sum_of_digits = sum(int(digit) for digit in str(number))
    return number % sum_of_digits == 0

num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")

def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number

for num in range(1, 1001):
    if is_armstrong(num):
        print(num)

def power(x, n):
    return x ** n

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
result = power(x, n)
print(f"The value of {x} raised to the power {n} is: {result}")

import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = nCr(n, r)
print(f"The value of {n}C{r} is: {result}")

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  # Add the last digit to the total
        number //= 10  # Remove the last digit
    return total

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {result}")
