inteiro = int(input())

if (inteiro < 1 or inteiro > 1000):
    exit()
else:
    for i in range(1, inteiro+1):
        if (i % 2 != 0):
            print("{}".format(i))