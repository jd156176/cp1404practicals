MINIMUM_LENGTH = 5

password = input("Type Password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password is too short! Password must be at least {MINIMUM_LENGTH} characters.")
    password = input("Type Password: ")

for i in range(len(password)):
    print("*", end="")