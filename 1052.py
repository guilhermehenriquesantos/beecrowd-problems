meses = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

entrada = int(input())

for numero, nome in meses.items():
    if (numero == entrada):
        print(nome)