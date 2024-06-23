user_email = {}
email = input("Email: ")
while email != "":
    name = (" ".join(str(email.split("@")[0]).split("."))).title()
    option = input(f"Is your name {name}? (Y/n)").lower()
    if option == "n" or option == "no": 
        name = input("Name: ").title()
    user_email[name] = email
    email = input("Email: ")

for name,email in user_email.items():
    print(f"{name} ({email})")