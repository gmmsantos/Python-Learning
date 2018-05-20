while True:
    termo = int(input("Informe o termo a ser calculado: "))
    if termo < 0 or termo > 16:
        print("Informe um valor positivo ou menor que 16")
    elif termo == 0:
        break
    else:
        fat = 1
        i = 1
        while i <= termo:
            fat *= i
            i += 1
        print(fat)