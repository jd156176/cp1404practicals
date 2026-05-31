MINIMUM_LENGTH = 5

def main():
    password = get_password()

    print_symbol(password, "-")


def print_symbol(password: str, symbol: str):
    for i in range(len(password)):
        print(symbol, end="")


def get_password() -> str:
    password = input("Type Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password is too short! Password must be at least {MINIMUM_LENGTH} characters.")
        password = input("Type Password: ")
    return password


main()