for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.print a number of stars.
num_stars = int(input("How many stars? "))
print("*" * num_stars)

# d.print lines of increasing stars.
num_lines = int(input("How many lines? "))
for i in range(1, num_lines + 1):
    print("*" * i)
