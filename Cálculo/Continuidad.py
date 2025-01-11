import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy import symbols, Piecewise, lambdify, limit, oo, sqrt

# Definición de símbolo
x = symbols("x")

# Función principal para analizar continuidad y límites
def analizar_continuidad(funcion, punto, intervalo=None):
    """
    Analiza la continuidad y los límites de una función en un punto dado y opcionalmente en un intervalo.
    
    Args:
    - funcion: Función simbólica (incluyendo funciones a trozos).
    - punto: Punto en el que se analizará la continuidad.
    - intervalo: Tupla (a, b) para evaluar la continuidad en un intervalo.
    
    Returns:
    - Gráfica de la función y análisis en la terminal.
    """
    # Convertir la función simbólica a una función numérica segura
    def funcion_segura(x_val):
        try:
            return float(funcion.subs(x, x_val))
        except:
            return np.nan

    # Evaluación de límites y valor en el punto
    limite_izquierda = limit(funcion, x, punto, dir='-')
    limite_derecha = limit(funcion, x, punto, dir='+')
    valor_funcion = funcion.subs(x, punto)

    # Análisis en el punto
    print(f"Análisis de continuidad en x = {punto}:")
    print(f"Límite por la izquierda: {limite_izquierda}")
    print(f"Límite por la derecha: {limite_derecha}")
    print(f"Valor de la función en x = {punto}: {valor_funcion}")

    if limite_izquierda == limite_derecha == valor_funcion:
        print("La función es continua en x =", punto)
    else:
        print("La función no es continua en x =", punto)
        if limite_izquierda != limite_derecha:
            print("Tipo de discontinuidad: Discontinuidad de salto finito.")
        elif limite_izquierda == limite_derecha != valor_funcion:
            print("Tipo de discontinuidad: Discontinuidad evitable.")
        else:
            print("Tipo de discontinuidad: Otra (por ejemplo, infinita).")

    # Análisis opcional en un intervalo
    if intervalo:
        print(f"\nAnálisis de continuidad en el intervalo {intervalo}:")
        es_continua = True
        for val in np.linspace(intervalo[0], intervalo[1], 100):
            if not np.isfinite(funcion_segura(val)):
                es_continua = False
                break
        if es_continua:
            print("La función es continua en el intervalo", intervalo)
        else:
            print("La función no es continua en el intervalo", intervalo)

    # Generar gráfica
    print("\nGenerando gráfica de la función...")
    x_vals = np.linspace(intervalo[0], intervalo[1], 1000) if intervalo else np.linspace(punto - 2, punto + 2, 500)
    y_vals = np.array([funcion_segura(val) for val in x_vals])

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue")
    plt.axvline(punto, color="red", linestyle="--", label=f"x = {punto}")
    plt.scatter([punto], [valor_funcion], color="green", zorder=5, label="Valor en el punto")
    plt.title("Gráfica de la función y análisis de continuidad")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
    plt.legend()
    plt.grid()
    plt.show()

# Ejemplos de uso

# Ejemplo 1: Función a trozos con discontinuidad de salto finito
funcion1 = Piecewise((x**2 + 5, x < 2), (1/2, x == 2), (3 + x**3, x > 2))
analizar_continuidad(funcion1, punto=2, intervalo=(-1, 3))

# Ejemplo 2: Función a trozos con discontinuidad evitable
funcion2 = Piecewise(((x**2 - 1) / (x - 1), x != 1), (3, x == 1))
analizar_continuidad(funcion2, punto=1, intervalo=(0, 2))

# Ejemplo 3: Función continua en todo el intervalo
funcion3 = x**2
analizar_continuidad(funcion3, punto=0, intervalo=(-5, 5))

# Ejemplo 4: Función con raíz cuadrada (para problemas de dominio)
funcion4 = Piecewise((2 * x - 3, x >= 2), (sqrt(2 - x), x < 2))
analizar_continuidad(funcion4, punto=2, intervalo=(1, 3))
