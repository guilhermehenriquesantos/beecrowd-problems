a, b, c = map (int, input().split())

array = [a, b, c]
desordenado = array.copy()
array.sort()

for i in array:
    print(i)

print()

for i in desordenado:
    print(i)
