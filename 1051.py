def calcular_8(renda):
    imposto_sobre8p = (renda - 2000.00) * 0.08
    return imposto_sobre8p

def calcular_18(renda):
    imposto_sobre_8p = calcular_8(3000.00)
    imposto_sobre_18p = (renda - 3000.00) * 0.18
    return imposto_sobre_8p + imposto_sobre_18p

def calcular_28(renda):
    imposto_sobre_18p = calcular_18(4500.00)
    imposto_sobre_28p = (renda - 4500.00) * 0.28
    return imposto_sobre_18p + imposto_sobre_28p

renda = float(input())

renda_arredondada = int (renda * 100) / 100.0

if (renda_arredondada >= 0.00 and renda_arredondada <= 2000.00):
    print("Isento")

elif (renda_arredondada > 2000.00 and renda_arredondada <= 3000.00):
    valor = calcular_8(renda_arredondada)
    print("R$ {:.2f}".format(valor))

elif (renda_arredondada > 3000.00 and renda_arredondada <= 4500.00):
    valor = calcular_18(renda_arredondada)
    print("R$ {:.2f}".format(valor))

elif (renda_arredondada > 4500.00):
    valor = calcular_28(renda_arredondada)
    print("R$ {:.2f}".format(valor))