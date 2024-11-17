N = int(input())
fatorial = 1

if (0 < N < 13):
    while (N >= 1):
        fatorial = fatorial * N
        N -= 1

print(fatorial)