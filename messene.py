def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    i = 2
    while len(primos) < n:
        if es_primo(i):
            primos.append(i)
        i += 1
    return primos

def primos_de_mersenne(n_primos):
    primos = primeros_n_primos(n_primos)
    primos_mersenne = []
    
    for p in primos:
        mersenne = 2 ** p - 1
        if es_primo(mersenne):
            primos_mersenne.append(mersenne)
    
    return primos_mersenne

# Obtener los primos de Mersenne usando los primeros 20 números primos
resultado = primos_de_mersenne(20)
print("Los números primos de Mersenne basados en los primeros 20 números primos son:", resultado)
