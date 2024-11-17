N = int(input())
fibonacci = []

if (N < 46):
    for i in range (0,46):
        if (len(fibonacci) < 2):
            fibonacci.append(i)
        else:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        if (len(fibonacci) == N):
            break

print(" ".join(map(str,fibonacci)))
