a = 80000
b = 200000
age = 0
while a <= b:
    a *= 1.03
    b *= 1.015
    age += 1
print("It'll take %d years to be same population" %age)