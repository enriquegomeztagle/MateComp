def ordenamiento_burbuja(arreglo):
    # Esta función implementa el algoritmo de ordenamiento por burbuja.
    # El algoritmo compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto.
    # Este proceso se repite hasta que el arreglo está completamente ordenado.

    longitud = len(arreglo)  # Almacena la cantidad de elementos en el arreglo.
    
    # Bucle externo que controla el número de pasadas completas a través del arreglo.
    for i in range(longitud - 1):
        # Bucle interno que avanza a través de los elementos que aún no han sido colocados en su posición final.
        for j in range(longitud - i - 1):
            # Compara el elemento actual con el siguiente en el arreglo.
            if arreglo[j] > arreglo[j + 1]:
                # Si el elemento actual es mayor que el siguiente, los intercambia.
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                
    # Una vez completados los bucles, el arreglo está ordenado y la función lo devuelve.
    return arreglo

# Arreglo de ejemplo para demostrar el funcionamiento del algoritmo.
arreglo_ejemplo = [5, 2, 3, 1, 4]
print("Arreglo sin ordenar:")
print(arreglo_ejemplo)  # Muestra el arreglo original sin ordenar.

# Llama a la función de ordenamiento por burbuja y almacena el resultado en 'arreglo_ordenado'.
arreglo_ordenado = ordenamiento_burbuja(arreglo_ejemplo)

print("Arreglo ordenado:")  # Indica que a continuación se mostrará el arreglo ordenado.
print(arreglo_ordenado)  # Muestra el arreglo ya ordenado.
