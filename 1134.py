ALCOOL = []
GASOLINA = []
DIESEL = []

while (True):
    combustivel = int(input())

    if (combustivel == 1):
        ALCOOL.append(1)
    elif (combustivel == 2):
        GASOLINA.append(1)
    elif (combustivel == 3):
        DIESEL.append(1)
    elif (combustivel == 4):
        break

print("MUITO OBRIGADO")
print("Alcool: {}".format(len(ALCOOL)))
print("Gasolina: {}".format(len(GASOLINA)))
print("Diesel: {}".format(len(DIESEL)))