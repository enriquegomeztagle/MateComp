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

# Función para calcular el Error Local de Truncamiento
def calcular_elt(f, y_analitica, y0, t0, tn, h, metodo):
    t_values = np.arange(t0, tn, h)
    y_values = metodo(f, y0, t0, t_values[-1] + h, int((tn - t0) / h))[1]
    y_exact = y_analitica(t_values)
    elt = np.abs(y_exact - y_values[:-1])
    return t_values, elt

# Función para calcular el Error Global de Truncamiento
def calcular_egt(f, y_analitica, y0, t0, tn, h, metodo):
    t_final = tn
    y_final_aprox = metodo(f, y0, t0, tn, int((tn - t0) / h))[1][-1]
    y_final_exact = y_analitica(t_final)
    egt = np.abs(y_final_exact - y_final_aprox)
    return egt

# Cálculo de errores para diferentes tamaños de paso
h_values = [0.1, 0.05, 0.01, 0.005, 0.001]
elt_euler = []
egt_euler = []
elt_rk2 = []
egt_rk2 = []

for h in h_values:
    _, elt_temp = calcular_elt(f, solucion_analitica, y0, t0, tn, h, euler_method)
    elt_euler.append(np.mean(elt_temp))
    egt_euler.append(calcular_egt(f, solucion_analitica, y0, t0, tn, h, euler_method))

    _, elt_temp = calcular_elt(f, solucion_analitica, y0, t0, tn, h, rk2_method)
    elt_rk2.append(np.mean(elt_temp))
    egt_rk2.append(calcular_egt(f, solucion_analitica, y0, t0, tn, h, rk2_method))

# Gráficos de ELT y EGT
plt.figure(figsize=(12, 6))

# Gráfico de ELT
plt.subplot(1, 2, 1)
plt.plot(h_values, elt_euler, label='ELT Euler', marker='o')
plt.plot(h_values, elt_rk2, label='ELT RK2', marker='o')
plt.xlabel('Tamaño del paso (h)')
plt.ylabel('Error Local de Truncamiento')
plt.title('ELT para Euler vs RK2')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)

# Gráfico de EGT
plt.subplot(1, 2, 2)
plt.plot(h_values, egt_euler, label='EGT Euler', marker='o')
plt.plot(h_values, egt_rk2, label='EGT RK2', marker='o')
plt.xlabel('Tamaño del paso (h)')
plt.ylabel('Error Global de Truncamiento')
plt.title('EGT para Euler vs RK2')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)

plt.tight_layout()
plt.show()
