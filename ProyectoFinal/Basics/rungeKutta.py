def rk2_method(f, y0, t0, tn, n):
    h = (tn - t0) / n
    t = t0
    y = y0
    
    for i in range(n):
        k1 = f(t, y)
        k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
        y += h * k2
        t += h
    
    return y

def f(t, y):
    return -2 * y + 4 * t

# Condiciones iniciales y parámetros
y0 = 1  # Valor inicial de y
t0 = 0  # Tiempo inicial
tn = 2  # Tiempo final
n = 10  # Número de pasos

approximation = rk2_method(f, y0, t0, tn, n)
print("Aproximación de y(t) en t =", tn, "es", approximation)
