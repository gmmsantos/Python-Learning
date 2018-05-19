tam = float(input("Enter meters square value: "))
litros = (tam / 6.0) * 1.1 #folga de 10%
lata18 = int(litros / 18)
lata3 = int(litros / 3.6)
if (lata18 % 18 != 0):
    lata18 = lata18 + 1
print("Voce devera comprar", lata18, "latas")
print("O valor total:", lata18 * 80)

if lata3 % 3.6 != 0:
    lata3 += 1
print("Voce devera comprar", lata3, "latas")
print("O valor total:", lata3 * 25)

# Calculo misturando latas e galoes
mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print("Latas:", lata18, '. Valor:', lata18 * 80)
print("Galoes:", lata3, '. Valor:', lata3 * 25)
print("Latas:", mixLatas, 'e', mixGaloes, '. Valor: ', (mixLatas * 80)+(mixGaloes*25))
