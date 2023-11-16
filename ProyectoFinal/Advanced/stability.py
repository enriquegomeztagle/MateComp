import numpy as np
import matplotlib.pyplot as plt

# Método de Euler
def euler_method(f, y0, t0, tn, n):
    h = (tn - t0) / n
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])

    return t_values, y_values

# Método Runge-Kutta de segundo orden (RK2)
def rk2_method(f, y0, t0, tn, n):
    h = (tn - t0) / n
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        k1 = f(t_values[i - 1], y_values[i - 1])
        k2 = f(t_values[i - 1] + 0.5 * h, y_values[i - 1] + 0.5 * h * k1)
        y_values[i] = y_values[i - 1] + h * k2

    return t_values, y_values

# Función diferencial donde Euler tiende a ser inestable
def f_unstable(t, y):
    return y - t**2 + 1

# Solución analítica de la ecuación diferencial
def solucion_analitica_unstable(t):
    return (t + 1)**2 - 0.5 * np.exp(t)

# Parámetros iniciales
t0, tn, y0 = 0, 2, 0.5

# Tamaños de paso para comparar
h_values = [0.02, 0.05, 0.1, 0.2]

plt.figure(figsize=(12, 8))

for i, h in enumerate(h_values, 1):
    t_values = np.arange(t0, tn + h, h)
    y_exact = solucion_analitica_unstable(t_values)

    # Soluciones Euler
    y_values_euler = euler_method(f_unstable, y0, t0, tn, int((tn - t0) / h))[1]

    # Soluciones RK2
    y_values_rk2 = rk2_method(f_unstable, y0, t0, tn, int((tn - t0) / h))[1]

    # Gráficos
    plt.subplot(2, 2, i)
    plt.plot(t_values, y_exact, label='Solución analítica', color='blue')
    plt.plot(t_values, y_values_euler, label='Euler h=' + str(h), linestyle='--', color='orange')
    plt.plot(t_values, y_values_rk2, label='RK2 h=' + str(h), linestyle='-.', color='green')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(f'Solución con h = {h}')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
