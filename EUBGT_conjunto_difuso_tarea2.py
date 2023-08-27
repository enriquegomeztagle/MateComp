"""
El código que se presenta a continuación es una sencilla aplicación para controlar la temperatura
y la humedad de una habitación. Se definen los conjuntos difusos de temperatura y humedad.
Cada conjunto difuso está definido por su limite inferior, superior y su pendiente respectivamente
(recordar que la pendiente depende de la aplicación de que se este efectuando, no se preocupen
muevan esos valores para que vean que resultados refleja). La pendiente mide el cambio de
transición desde el grado de pertenencia 0 del conjunto difuso a su grado de pertenencia 1 (cuando
comentamos en clase acerca de la producción de los pistones y del grado en el que un cantante
es famoso).
"""

import numpy as np  # Biblioteca para cálculos matriciales


def conjunto_difuso(x, a, b, c):
    """
    Esta función implementa un algoritmo de mapeo de conjuntos difusos

    Args:
        x: El valor de entrada.
        a: El límite inferior del conjunto difuso.
        b: El límite superior del conjunto difuso.
        c: La pendiente del conjunto difuso, arreglo de función gamma.

    Returns:
        El valor de salida del mapeo del conjunto difuso.
    """
    if x < a:  # Si el valor de entrada es menor que el límite inferior.
        return 0  # El grado de pertenencia es 0.
    elif x > b:  # Si el valor de entrada es mayor que el límite superior.
        return 1  # El grado de pertenencia es 1.
    else:  # Si el valor de entrada está entre a y b.
        return (x - a) / (
            b - a
        )  # Calculamos el grado de pertenencia usando función trapezoidal.


def control_difuso(temperatura, humedad):
    """
    Esta función implementa un algoritmo de control borroso.

    Args:
        temperatura: La temperatura
        humedad: la humedad

    Returns:
        El valor de salida del algoritmo de control borroso.
    """
    # Definir los conjuntos difusos para la temperatura.
    frio = (
        0,
        15,
        0,
    )  # Definir el conjunto difuso "frío" con límites inferior y superior y pendiente.
    templado = (15, 25, 1)  # Definir el conjunto difuso "templado".
    caliente = (25, 35, 0)  # Definir el conjunto difuso "caliente".

    # Definir los conjuntos difusos para la humedad
    seco = (0, 40, 0)  # Definir el conjunto difuso "seco" para humedad.
    normal = (40, 60, 1)  # Definir el conjunto difuso "normal".
    humedo = (60, 100, 0)  # Definir el conjunto difuso "húmedo".

    # Calcular los grados de pertenencia de los valores de entrada. (Se está desempaquetando la tupla)
    temperatura_frio = conjunto_difuso(
        temperatura, *frio
    )  # Calcular grado de pertenencia al conjunto "frío".
    temperatura_templado = conjunto_difuso(
        temperatura, *templado
    )  # Calcular grado de pertenencia al conjunto "templado".
    temperatura_caliente = conjunto_difuso(
        temperatura, *caliente
    )  # Calcular grado de pertenencia al conjunto "caliente".

    humedad_seco = conjunto_difuso(
        humedad, *seco
    )  # Calcular grado de pertenencia al conjunto "seco".
    humedad_normal = conjunto_difuso(
        humedad, *normal
    )  # Calcular grado de pertenencia al conjunto "normal".
    humedad_humedo = conjunto_difuso(
        humedad, *humedo
    )  # Calcular grado de pertenencia al conjunto "húmedo".

    # Aplicar las reglas de conjuntos difusos usando multiplicación de matrices.
    # Recordar que la multiplicación entre matrices no es conmutativa.
    reglas_difusas = np.array(
        [humedad_seco, humedad_normal, humedad_humedo]
    )  # Crear matriz de reglas difusas para la humedad.
    peso_temperatura = np.array(
        [temperatura_frio, temperatura_templado, temperatura_caliente]
    )  # Crear matriz de pesos de temperatura.
    salida = np.dot(
        reglas_difusas, peso_temperatura
    )  # Realizar multiplicación matricial para obtener salida difusa.

    return salida  # Devolver el valor de salida difusa.


def principal():
    # Establecer los valores de entrada.
    temperatura = 25  # Definir un valor de temperatura.
    humedad = 50  # Definir un valor de humedad.

    salida = control_difuso(temperatura, humedad)  # Calcular el valor de salida difusa.

    print(salida)  # Imprimir el valor de salida.


if __name__ == "__main__":
    principal()  # Llamar a la función principal si se ejecuta como script.


"""
A) Con base al siguiente código aplicado a conjuntos difusos, ejecutarlo y escribir con tus
propias palabras, ¿cómo ejecuta el proceso el código?, recomendación coloca diferentes
valores en los arreglos, y observa como se comporta con base a lo modificado.
"""

"""
FUNCIONES:
- Función conjunto_difuso(x,a,b,c):
Recibe un valor de entrada x y los límites (LI & LS) del conjunto (a, b respectivamente) y al 
final una pendiente C.
	Se calcula el grado de pertenencia de x al conjunto difuso con una función trapezoidal. Si 'x' 
está por debajo de a, se asigna 0, si está por encima, se asigna 1 y si no, se calcula de forma lineal.

- Función control_difuso(temperatura, humedad):
Define conjuntos difusos para cada uno de los parámetros y calcula el grado de pertenencia de esos 
valores de entrada a estos conjuntos a través de la función anterior. Después combina los grados de 
pertenencia a través de reglas difusas y genera una salida difusa.

- Función principal():
Establece los valores de entrada para cada parámetro y llama a la función control_difuso(temperatura, humedad)
para obtener el cálculo de la salida difusa.

PROCESO:
- Se definen los conjuntos difusos: Cada uno con 3 categorías: frío, templado y caliente para la temperatura y
seco, normal y húmedo para la humedad. Cada conjunto está formado por 3 valores (LI, LS, M) (límites y pendiente)
- Se evaluan los grados de pertenencia: Cada valor de entrada se compara con los límites de los conjuntos difusos
correspondientes y devuelve 1 o 0. Esto es que tanto se ajusta cada valor a los conjuntos.
- Se aplican reglas difusas: Se combinan los grados de pertenencia de cada parámetros y se obtiene una salida 
difusa.
- Se calcula la salida difusa: Se multiplica la matriz resultaante por el vector de grados de pertenencia de
temperatura. Así se ponderan los grados de pertenencia de temperatura y humedad. Refleja la acción que se
debe tomar de acuerdo a ciertas condiciones.
"""


"""
Funcionalidades adicionales por añadir:
- Defuzzificación: convertir la salida difusa en un número usando el centroide de la salida.
- Ajustar parámetros de conjuntos difusos: para observar comportamientos distintos.
- Agregar mensaje descriptivo: al tomar una desición, lanzar un mensaje.
"""

import numpy as np


def fuzzy_set(x, a, b, c):
    if x < a:
        return 0
    elif x > b:
        return 1
    else:
        return (x - a) / (b - a)


def fuzzy_control(temperature, humidity):
    cold = (0, 15, 0)
    mild = (15, 25, 1)
    hot = (25, 35, 0)

    dry = (0, 40, 0)
    normal_humidity = (40, 60, 1)
    humid = (60, 100, 0)

    temperature_cold = fuzzy_set(temperature, *cold)
    temperature_mild = fuzzy_set(temperature, *mild)
    temperature_hot = fuzzy_set(temperature, *hot)

    humidity_dry = fuzzy_set(humidity, *dry)
    humidity_normal = fuzzy_set(humidity, *normal_humidity)
    humidity_humid = fuzzy_set(humidity, *humid)

    fuzzy_rules = np.array([humidity_dry, humidity_normal, humidity_humid])
    temperature_weights = np.array(
        [temperature_cold, temperature_mild, temperature_hot]
    )
    output = np.dot(fuzzy_rules, temperature_weights)

    return output


def defuzzification(output_fuzzy):
    possible_values = np.arange(0, 101)  # Possible output variable values
    centroid = np.sum(possible_values * output_fuzzy) / np.sum(output_fuzzy)
    return centroid


def interpret_output(value):
    if value <= 30:
        return "Turn off system"
    elif value <= 70:
        return "Maintain current state"
    else:
        return "Turn on system"


def main():
    temperature = 25
    humidity = 50

    fuzzy_output = fuzzy_control(temperature, humidity)
    defuzzified_value = defuzzification(fuzzy_output)
    decision = interpret_output(defuzzified_value)

    print("Fuzzy Output:", fuzzy_output)
    print("Defuzzified Value:", defuzzified_value)
    print("Decision:", decision)


if __name__ == "__main__":
    print("\n-------------------\nWith modifications: ")
    main()


"""
OUTPUT
1.5

-------------------
With modifications:
Fuzzy Output: 1.5
Defuzzified Value: 5050.0
Decision: Turn on system
[Finished in 144ms]
"""
