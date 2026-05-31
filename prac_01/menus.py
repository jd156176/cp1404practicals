name = input("Enter Name: ")

MENU_STRING = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU_STRING)

menu_choice = input(">>> ")
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid Choice")
    print(MENU_STRING)
    menu_choice = input(">>> ")
print("Finished")