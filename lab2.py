def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci(n)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"The factorial of {num} is: {factorial(num)}")

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiplication_table(num)

import math

def gcd(x, y):
    return math.gcd(x, y)

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
