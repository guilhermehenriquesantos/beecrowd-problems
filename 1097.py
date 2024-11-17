I = 0
J = 1
J_inicial = 1

while(I <= 2):
    if (I - int(I) > 0):
        print('I={} J={}'.format(I,J))
    else:
        print('I={} J={}'.format(int(I),int(J)))
    J += 1

    if (J == (J_inicial + 3)):
        J = float('{:.2f}'.format(J - 3 + 0.2))
        J_inicial = J
        I = float('{:.2f}'.format(I + 0.2))
