AGENDA = {61:"Brasilia", 71:"Salvador", 11:"Sao Paulo", 21:"Rio de Janeiro", 32:"Juiz de Fora", 19:"Campinas", 27:"Vitoria", 31:"Belo Horizonte"}

try:
    ddd = int(input())

    if ddd not in AGENDA.keys():
        print("DDD nao cadastrado")

    for key, value in AGENDA.items():
        if (ddd == key):
            print(value)

except Exception as error:
    print("DDD nao cadastrado")
