n = 50

if n <= 3:
    print("El número debe ser mayor que 3.")
    exit()

maximo = (n - 3) // 2
esPrimo = [True] * (maximo + 1)

i = 0
while (2 * i + 3) * (2 * i + 3) <= n:
    k = i + 1
    if esPrimo[i]:
        while (2 * k + 1) * (2 * i + 3) <= n:
            esPrimo[((2 * k + 1) * (2 * i + 3) - 3) // 2] = False
            k += 1
    i += 1

primos = [2, 3]
for j in range(1, maximo + 1):
    if esPrimo[j]:
        primos.append(2 * j + 3)

print(", ".join(map(str, primos)))
