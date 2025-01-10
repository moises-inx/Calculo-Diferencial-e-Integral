import sympy as sp
import matplotlib
matplotlib.use('TkAgg')  # Usar un backend interactivo para mostrar gráficos
import matplotlib.pyplot as plt
import numpy as np

def calcular_y_graficar_limite(expresion_str, variable_str, punto, direccion='ambos'):
    """
    Calcula el límite de la expresión dada y grafica la función alrededor del punto dado.

    Parámetros:
    expresion_str (str): La expresión como cadena, por ejemplo, "sin(x)/x".
    variable_str (str): La variable en la expresión, por ejemplo, "x".
    punto (float o str): El punto en el que se calcula el límite. Usar "oo" para infinito.
    direccion (str): Dirección para el límite ('ambos', 'izquierda' o 'derecha').

    Retorna:
    None
    """
    # Definir el símbolo y analizar la expresión
    x = sp.symbols(variable_str)
    expresion = sp.sympify(expresion_str)

    # Determinar la dirección del límite
    if direccion == 'izquierda':
        resultado_limite = sp.limit(expresion, x, punto, dir='-')
    elif direccion == 'derecha':
        resultado_limite = sp.limit(expresion, x, punto, dir='+')
    else:
        limite_izquierda = sp.limit(expresion, x, punto, dir='-')
        limite_derecha = sp.limit(expresion, x, punto, dir='+')
        resultado_limite = sp.limit(expresion, x, punto)

    # Mostrar información del límite
    print("Expresión:", expresion)
    print("Punto:", punto)
    if direccion == 'ambos':
        print("Límite por la izquierda:", limite_izquierda)
        print("Límite por la derecha:", limite_derecha)
        print("Límite (global):", resultado_limite)
    else:
        print(f"Límite ({direccion}):", resultado_limite)

    # Verificar si el límite existe (izquierda y derecha deben ser iguales si la dirección es 'ambos')
    if direccion == 'ambos' and limite_izquierda != limite_derecha:
        print("El límite no existe porque los límites por la izquierda y por la derecha no son iguales.")
    elif resultado_limite == sp.oo:
        print("El límite es infinito.")
    elif resultado_limite == -sp.oo:
        print("El límite es menos infinito.")
    else:
        print("El límite existe y es:", resultado_limite)

    # Generar una gráfica de la función
    try:
        f_lambdified = sp.lambdify(x, expresion, 'numpy')

        # Definir el rango para la gráfica
        if punto == sp.oo:
            x_vals = np.linspace(1, 10, 400)
        elif punto == -sp.oo:
            x_vals = np.linspace(-10, -1, 400)
        else:
            x_vals = np.linspace(punto - 2, punto + 2, 400)

        y_vals = f_lambdified(x_vals)

        # Graficar la función
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=str(expresion))
        plt.axvline(x=punto, color='r', linestyle='--', label=f'x = {punto}')
        plt.title(f'Gráfica de {expresion_str} y su límite en x = {punto}')
        plt.xlabel(variable_str)
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()  # Mostrar la gráfica en pantalla

    except Exception as e:
        print("Error al generar la gráfica:", e)

# Ejemplo de uso
    # Dentro de las primeras comillas "", se coloca la función, luego, en las siguientes comillas, se coloca la variable y posteriormente se pone hacia donde tiende el límite
calcular_y_graficar_limite("x * sin(1/x)", "x", 0)
calcular_y_graficar_limite("x * sin(1/x)", "x", 0, direccion='derecha')
calcular_y_graficar_limite("x * sin(1/x)", "x", 0, direccion='izquierda')
