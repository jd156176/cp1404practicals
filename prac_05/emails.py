"""
Emails
Estimated time: 20 Minutes
Actual time: 22 minutes 43 seconds
"""
email_to_name = {}

email = input("Email: ")
while email != "":
    prefix = email.split("@")[0]
    inferred_name = " ".join(prefix.split(".")).title()

    confirmation = input(f"Is your name {inferred_name}? (Y/n) ").strip().lower()

    if confirmation == "" or confirmation == "y":
        name = inferred_name
    else:
        name = input("Name: ").title()

    email_to_name[email] = name

    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name:{len(max(email_to_name.values(), key=len))}} {email}")