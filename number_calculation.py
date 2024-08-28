number = input("Enter a number: ")

# Convert the input to an integer
number = int(number)

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")