# import itertools

# palabra = "COTORRO"

# # a) Eliminando tipos repetidos:
# permutaciones_sin_repeticiones = list(itertools.permutations(set(palabra), len(set(palabra))))
# print("Número de permutaciones eliminando tipos repetidos:", len(permutaciones_sin_repeticiones))

# # b) Considerando que todas son diferentes, aun cuando se trate de la misma letra:
# permutaciones_con_repeticiones = list(itertools.permutations(palabra, len(palabra)))
# print("Número de permutaciones considerando todas las letras diferentes:", len(permutaciones_con_repeticiones))

# import math

# palabra = "MATEMATICAS"
# n = len(palabra)

# # a) Permutaciones totales de MATEMATICAS:
# total_permutaciones = math.factorial(n) / (math.factorial(2) * math.factorial(3) * math.factorial(2))
# print(f"Total de permutaciones: {int(total_permutaciones)}")

# # b) Permutaciones que comienzan con M:
# # Quitamos una M y calculamos las permutaciones del resto de la palabra.
# perm_m = math.factorial(n-1) / (math.factorial(2) * math.factorial(3) * math.factorial(2))
# print(f"Permutaciones que comienzan con M: {int(perm_m)}")

# # c) Permutaciones que comienzan con A:
# # Quitamos una A y calculamos las permutaciones del resto de la palabra.
# perm_a = math.factorial(n-1) / (math.factorial(2) * math.factorial(2) * math.factorial(2))
# print(f"Permutaciones que comienzan con A: {int(perm_a)}")

# import math

# n = 14  # Total de jóvenes profesionistas
# k = 8   # Número de profesionistas a seleccionar

# # Calculamos el número de combinaciones
# combinaciones = math.comb(n, k)

# print(f"El número de maneras de seleccionar a los 8 profesionistas de un grupo de 14 es: {combinaciones}")

# import math

# n = 5  # Total de dígitos disponibles
# k = 3  # Número de dígitos a seleccionar para formar el número

# # Calculamos el número de permutaciones
# permutaciones = math.perm(n, k)

# print(f"El número de números de tres cifras diferentes que se pueden formar con los dígitos 1,2,3,4,5 es: {permutaciones}")

# Dígitos disponibles
digitos = [0,1,2,3,4,5]

# Número de maneras de seleccionar el primer dígito (sin el 0)
primer_digito = len(digitos) - 1

# Número de maneras de seleccionar el segundo dígito
segundo_digito = len(digitos) - 1

# Número de maneras de seleccionar el tercer dígito
tercer_digito = len(digitos) - 2

# Calculamos el total de permutaciones
permutaciones = primer_digito * segundo_digito * tercer_digito

print(f"El número de números de tres cifras diferentes que se pueden formar con los dígitos 0,1,2,3,4,5 es: {permutaciones}")
