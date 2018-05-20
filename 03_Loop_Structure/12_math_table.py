n = int(input("Informe qual tabuada qr saber: "))
i = 1
if n >= 1 and n <= 10:
    print("Tabuada do %d: " %n)
    for i in range(1, 11):
        print("%d X %d = %d" %(n, i, n*i))
        i += 1
else:
    print("Informe uma tabuada entre 1 e 10")