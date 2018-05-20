while True:
    name = input("Enter your name: ")
    if len(name) > 3:
        break
    else:
        print("Name must be more than 3 char")
        print("Enter a NEW name")

while True:
    age = int(input("Enter your age: "))
    if age >= 0 and age <= 150:
        break
    else:
        print("Age must be between 0 and 150")
        print("Enter a NEW age")
        
while True:
    wage = float(input("Enter your wage: "))
    if wage > 0:
        break
    else:
        print("Wage must be more than 0")
        print("Enter a NEW value")

while True:
    gender = input("Enter your gender (M or F): ")
    if gender.upper() == "M" or gender == "F":
        break
    else:
        print("Enter a valid value")
        
while True:
    ms = input("Enter your Marital Status(S - C - V - D): ")
    if ms.upper() == "S" or "C" or "V" or "D":
        break
    else:
        print("Enter a valid Marital Status")