name = input("Enter your username: ")
while True:
    passwd = input("Enter your password: ")
    if name.upper() != passwd.upper():
        print("Successful Registration")
        break
    else:
        print("Password must be different from your username!")
        print("Enter a NEW password")