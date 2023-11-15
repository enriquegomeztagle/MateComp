import numpy as np
import matplotlib.pyplot as plt

# Definición del método Runge-Kutta de segundo orden (RK2)
def rk2_method(f, y0, t0, tn, n):
    h = (tn - t0) / n
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        k1 = f(t_values[i-1], y_values[i-1])
        k2 = f(t_values[i-1] + h, y_values[i-1] + k1 * h)
        y_values[i] = y_values[i-1] + (k1 + k2) / 2 * h

    return t_values, y_values

# Función para graficar los métodos
def plot_methods(t_values, y_approx, y_exact, h, ax):
    ax.plot(t_values, y_exact, label='Solución analítica', color='blue')
    ax.plot(t_values, y_approx, label=f'Método RK2 (h={h})', linestyle='--', color='orange')
    ax.set_xlabel('t')
    ax.set_ylabel('y')
    ax.legend()

# Funciones para la EDO y la solución analítica
def f(t, y):
    return -2 * y + 4 * t

def solucion_analitica(t):
    return 2 * t - 0.5 * np.exp(-2 * t)

# Crear una figura con subplots para diferentes valores de h
fig, axs = plt.subplots(4, 4, figsize=(20, 16))  # Ajusta el tamaño de la figura si es necesario
h_values = [0.5**(i+1) for i in range(4)]  # Diferentes valores para el tamaño del paso

for i in range(4):
    for j in range(4):
        h = h_values[i] * 0.1**(j+1)
        t_values, y_values = rk2_method(f, 1, 0, 2, int(2/h))
        y_exact = solucion_analitica(t_values)
        ax = axs[i, j]
        plot_methods(t_values, y_values, y_exact, h, ax)
        ax.title.set_text(f'h = {h:.1e}')  # Formato científico para el título

plt.tight_layout()
plt.show()
