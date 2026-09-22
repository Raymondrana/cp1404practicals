"""
MINIMUM_LENGTH = 8

password = input("Enter your password: ")

while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
    password = input("Enter your password: ")

print("*" * len(password))
"""



MINIMUM_LENGTH = 8

def main():

    password = get_password()

    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Enter your password: ")

    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
        password = input("Enter your password: ")
    return password


main()