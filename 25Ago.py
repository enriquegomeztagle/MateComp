def fuzzy_set_mapping(x,a,b,c):
    """
    Esta función implementa una algoritmo de mapeo de conjuntos difusos:

    Args:
    X: El valor de entrada.
    a: El límite inferior del conjunto difuso.
    b: El límite superior del conjunto difuso.
    c: La pendiente del conjunto difuso.

    Returns:
    El valor de salida del mapeo de conjunto difuso.
    """

    if x < a:
        return 0
    elif x > b:
        return 1
    else:
        return (x-a) / (b-a)
        

if __name__ == "__main__":
    X = 0.5
    A = 0
    B = 1
    C = 1

    print(fuzzy_set_mapping(X, A, B, C))
