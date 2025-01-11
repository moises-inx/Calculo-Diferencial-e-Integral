import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')  # Cambia el backend
import matplotlib.pyplot as plt

def calcular_y_graficar_limite(funcion_str, variable_str, punto):
    # Definir la variable y la función simbólica
    x = sp.Symbol(variable_str)
    funcion = sp.sympify(funcion_str)

    # Calcular límites laterales
    limite_izquierdo = sp.limit(funcion, x, punto, dir='-')
    limite_derecho = sp.limit(funcion, x, punto, dir='+')

    # Evaluar si el límite existe
    limite_central = sp.limit(funcion, x, punto)
    limite_existe = limite_izquierdo == limite_derecho == limite_central

    # Mostrar resultados en la consola
    print(f"Límite por la izquierda en x -> {punto}: {limite_izquierdo}")
    print(f"Límite por la derecha en x -> {punto}: {limite_derecho}")
    if limite_existe:
        print(f"El límite en x -> {punto} es: {limite_central}")
    else:
        print(f"El límite en x -> {punto} no existe.")

    # Crear datos para la gráfica
    x_vals_izq = np.linspace(punto - 2, punto, 500, endpoint=False)  # Valores hacia la izquierda del punto
    x_vals_der = np.linspace(punto, punto + 2, 500, endpoint=False)  # Valores hacia la derecha del punto
    x_vals = np.concatenate((x_vals_izq, x_vals_der))  # Unión de valores
    f_lambda = sp.lambdify(x, funcion, modules=["numpy"])  # Función evaluable en numpy

    # Calcular valores de la función
    y_vals_izq = f_lambda(x_vals_izq)
    y_vals_der = f_lambda(x_vals_der)

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='black', linewidth=0.8, linestyle="--")  # Línea horizontal en y=0
    plt.axvline(punto, color='black', linewidth=0.8, linestyle="--", label=f"x = {punto}")  # Línea vertical en x=punto

    # Gráficas por izquierda y derecha
    plt.plot(x_vals_izq, y_vals_izq, color='purple', label="Límite por izquierda")  # Límite por la izquierda
    plt.plot(x_vals_der, y_vals_der, color='red', label="Límite por derecha")  # Límite por la derecha

    # Marcador en el punto del límite (si existe)
    if limite_izquierdo.is_real and limite_derecho.is_real:
        plt.scatter([punto], [limite_izquierdo], color='purple', s=50, zorder=5, label="Valor por izquierda")
        plt.scatter([punto], [limite_derecho], color='red', s=50, zorder=5, label="Valor por derecha")

    # Configuración de la gráfica
    plt.title(f"Gráfica de {funcion_str} cerca de x = {punto}")
    plt.xlabel(variable_str)
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

# Ejemplo de uso
calcular_y_graficar_limite("x*abs(x)", "x", 0)
