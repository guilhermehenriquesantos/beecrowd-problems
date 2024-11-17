# -*- coding: utf-8 -*-

N = int(input())

if (N > 0 and N < 1000000):
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
    
    notas_um = int (resultado / 1)
    resultado = (resultado % 1)

    print(N)
    print("{} nota(s) de R$ 100,00".format(notas_cem))
    print("{} nota(s) de R$ 50,00".format(notas_cinquenta))
    print("{} nota(s) de R$ 20,00".format(notas_vinte))
    print("{} nota(s) de R$ 10,00".format(notas_dez))
    print("{} nota(s) de R$ 5,00".format(notas_cinco))
    print("{} nota(s) de R$ 2,00".format(notas_dois))
    print("{} nota(s) de R$ 1,00".format(notas_um))