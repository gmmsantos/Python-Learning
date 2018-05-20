n = int(input("Enter a value: "))
i = 2
primo = True
while i < n:
    if n % i == 0:
        primo = False
    i += 1
        
if primo:
    print("Numero é primo")
else:
    print("Não é primo")  