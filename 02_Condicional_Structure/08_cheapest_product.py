num1 = int(input("First n: "))
num2 = int(input("Second n: "))
num3 = int(input("Third n: "))

if num1 == num2 and num1 == num3:
    print("Same value")
else:
    if num1 < num2 and num1 < num3:
        print(num1)
    elif num2 < num3:
        print(num2)
    else:
        print(num3)