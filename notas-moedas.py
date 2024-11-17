N = float(input())
N = float("{:.2f}".format(N))

if (N >= 0.0 and N <= 1000000.00):
    resultado = N
    

    notas_cem = int (resultado / 100)
    resultado = (resultado % 100)
    
    notas_cinquenta = int (resultado / 50)
    resultado = (resultado % 50)
    
    notas_vinte = int (resultado / 20)
    resultado = (resultado % 20)
    
    notas_dez = int (resultado / 10)
    resultado = (resultado % 10)
    
    notas_cinco = int (resultado / 5)
    resultado = (resultado % 5)
    
    notas_dois = int (resultado / 2)
    resultado = (resultado % 2)
    
    #################################
    
    moedas_um_real = int (resultado / 1)
    resultado = resultado % 1

    moedas_cinquenta = int (resultado / 0.5)
    resultado = round (resultado % 0.5, 2)

    moedas_vinte_cinco = int (resultado / 0.25)
    resultado = round (resultado % 0.25, 2)

    moedas_dez = int (resultado / 0.10)
    resultado = round (resultado % 0.10, 2)

    moedas_cinco = int (resultado / 0.05)
    resultado = round (resultado % 0.05, 2)

    moedas_um_centavo = int (resultado / 0.01)
    resultado = round (resultado % 0.01, 2)

    print('NOTAS:')
    print("{} nota(s) de R$ 100.00".format(notas_cem))
    print("{} nota(s) de R$ 50.00".format(notas_cinquenta))
    print("{} nota(s) de R$ 20.00".format(notas_vinte))
    print("{} nota(s) de R$ 10.00".format(notas_dez))
    print("{} nota(s) de R$ 5.00".format(notas_cinco))
    print("{} nota(s) de R$ 2.00".format(notas_dois))

    print('MOEDAS:')
    print("{} moeda(s) de R$ 1.00".format(moedas_um_real))
    print("{} moeda(s) de R$ 0.50".format(moedas_cinquenta))
    print("{} moeda(s) de R$ 0.25".format(moedas_vinte_cinco))
    print("{} moeda(s) de R$ 0.10".format(moedas_dez))
    print("{} moeda(s) de R$ 0.05".format(moedas_cinco))
    print("{} moeda(s) de R$ 0.01".format(moedas_um_centavo))