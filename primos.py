def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

def procedimiento_principal():
    numero = int(input("Ingresa un número: "))
    
    if es_primo(numero):
        print(f"Es primo: {numero}")
    else:
        print(f"No es primo: {numero}")

# Llama al procedimiento principal para ejecutar el código
procedimiento_principal()
