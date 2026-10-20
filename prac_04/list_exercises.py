# Initialize an empty list called numbers
numbers = []

# Prompt the user 5 times to enter a number
for i in range(5):
    # Prompt the user and convert the input to a float (or int)
    num = float(input(f"Enter number {i + 1}: "))
    # Add the number to the list
    numbers.append(num)

# Output the information about the numbers exactly as requested
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

"""Security Checker"""
# List of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask the user for their username
user_input = input("Enter your username: ")

# Check authorization
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
