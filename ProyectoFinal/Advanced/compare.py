import numpy as np
import matplotlib.pyplot as plt

# Método de Euler (tu versión original)
def euler_method(f, y0, t0, tn, n):
    h = (tn - t0) / n
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])

    return t_values, y_values

# Método Runge-Kutta de segundo orden (RK2) (tu versión original)
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

# Función diferencial y solución analítica
def f(t, y):
    return -2 * y + 4 * t

def solucion_analitica(t):
    return 2 * t - 0.5 * np.exp(-2 * t)

# Tamaño del paso y cálculo de soluciones
h = 0.1
t0, tn, y0 = 0, 2, 1
t_values = np.arange(t0, tn + h, h)
y_exact = solucion_analitica(t_values)
t_values_euler, y_values_euler = euler_method(f, y0, t0, tn, int((tn - t0) / h))
t_values_rk2, y_values_rk2 = rk2_method(f, y0, t0, tn, int((tn - t0) / h))

# Gráfica de comparación
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_exact, label='Solución analítica', color='blue')
plt.plot(t_values_euler, y_values_euler, label='Método de Euler', linestyle='--', color='orange')
plt.plot(t_values_rk2, y_values_rk2, label='Método RK2', linestyle='-.', color='green')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Comparación de Soluciones Exactas vs. Aproximadas')
plt.legend()
plt.grid(True)
plt.show()
