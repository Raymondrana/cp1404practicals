# 1. Ask for name and write to file
out_file = open("name.txt", "w")
user_name = input("Enter your name: ")
out_file.write(user_name)
out_file.close()

# 2. Read name from file and print greeting
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers and add them
# Using 'with' and readline() to read exactly two individual lines
with open("numbers.txt", "r") as number_file:
    first_number = int(number_file.readline())
    second_number = int(number_file.readline())

result = first_number + second_number
print(result)

# 4. Total all numbers in the file
total = 0
with open("numbers.txt", "r") as number_file:
    for line in number_file:
        total += int(line)

print(total)