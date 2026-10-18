MINIMUM_LENGTH = 8
def main():
    password = get_password()
    hide_password(password)

def hide_password(password: str):
    print("*" * len(password))

def get_password() -> str:
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Password: ")
    return password

main()
