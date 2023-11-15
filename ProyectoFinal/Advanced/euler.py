import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t0, tn, n, solucion_analitica=None):
    h = (tn - t0) / n
    t_values = np.arange(t0, tn+h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])

    return t_values, y_values

def plot_methods(t_values, y_approx, y_exact, h, ax):
    ax.plot(t_values, y_exact, label='Solución analítica')
    ax.plot(t_values, y_approx, label=f'Método de Euler (h={h})', linestyle='--')
    ax.set_xlabel('t')
    ax.set_ylabel('y')
    ax.legend()

# TODO: UPDATE F
def f(t, y):
    return -2 * y + 4 * t

def solucion_analitica(t):
    return 2*t - 0.5*np.exp(-2*t)

fig, axs = plt.subplots(4, 4, figsize=(5, 4))
h_values = []
for i in range(4):
    for j in range(4):
        h_values.append(0.5**(i+1) * 0.1**(j+1))


for h, ax in zip(h_values, axs.flatten()):
    t_values, y_values = euler_method(f, 1, 0, 2, int(2/h), solucion_analitica)
    y_exact = solucion_analitica(t_values)
    plot_methods(t_values, y_values, y_exact, h, ax)

plt.tight_layout()
plt.show()
