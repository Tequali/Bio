import math
number = input("Enter a number: ")

# Convert the input to an integer
number = int(number)

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Check if the number is prime

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
        return True

if prime_number(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Check if the number is a perfect square

def is_perfect_square(number):
    return math.isqrt(number)**2 == number

if is_perfect_square(number):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")

print(number*number)