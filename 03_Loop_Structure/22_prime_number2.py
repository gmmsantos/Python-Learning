n = int(input("Enter a value: "))
i = 2
primo = True
while i < n:
    if n % i == 0:
        primo = False
        break
    i += 1
        
if primo:
    print("Numero é primo")
else:
    print("Não é primo")
    print("Os divisores sao: ")
    for i in range(2, n+1):
        if n % i == 0:
            print(i)