even = 0
odd = 0
for i in range(1, 11):
    n = int(input("Enter %d value : " %i))
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even: ", even)
print("Odd: ", odd)