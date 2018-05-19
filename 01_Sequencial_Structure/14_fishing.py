a = float(input("Enter the value fish weight: "))
if a < 50:
    print("Not overweight")
else:
    print("Overweight is:", a-50)
    print("You need to pay:", (a-50)*4, "$")