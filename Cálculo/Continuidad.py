import matplotlib
matplotlib.use("TkAgg")  # Configuración para evitar errores de visualización
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def estudiar_continuidad(funcion_str, variable_str, punto=None, intervalo=None):
    """
    Estudia la continuidad de una función en un punto o intervalo.
    """
    x = sp.Symbol(variable_str)
    funcion = sp.sympify(funcion_str)

    # Evaluación en un punto
    if punto is not None:
        limite_izquierdo = sp.limit(funcion, x, punto, dir='-')
        limite_derecho = sp.limit(funcion, x, punto, dir='+')
        valor_funcion = sp.limit(funcion, x, punto)

        print(f"Análisis de continuidad en x = {punto}:")
        print(f"Límite por la izquierda: {limite_izquierdo}")
        print(f"Límite por la derecha: {limite_derecho}")
        print(f"Valor de la función en x = {punto}: {valor_funcion}")

        if limite_izquierdo == limite_derecho == valor_funcion:
            print(f"La función es continua en x = {punto}.")
        else:
            print(f"La función NO es continua en x = {punto}.")
            if limite_izquierdo != limite_derecho:
                print("Tipo de discontinuidad: Discontinuidad de salto finito.")
            elif limite_izquierdo == limite_derecho and limite_derecho != valor_funcion:
                print("Tipo de discontinuidad: Discontinuidad evitable.")
            else:
                print("Tipo de discontinuidad: Discontinuidad infinita.")

    if intervalo is not None:
        a, b = intervalo
        print(f"\nAnálisis de continuidad en el intervalo ({a}, {b}):")
        puntos_discontinuidad = []
        continua = True

        for punto in np.linspace(a, b, 1000):
            limite_izquierdo = sp.limit(funcion, x, punto, dir='-')
            limite_derecho = sp.limit(funcion, x, punto, dir='+')
            valor_funcion = sp.limit(funcion, x, punto)

            if limite_izquierdo != limite_derecho or limite_derecho != valor_funcion:
                continua = False
                puntos_discontinuidad.append(punto)

        if continua:
            print(f"La función es continua en el intervalo ({a}, {b}).")
        else:
            print(f"La función NO es continua en el intervalo ({a}, {b}).")
            print(f"Puntos de discontinuidad detectados: {puntos_discontinuidad[:5]}{'...' if len(puntos_discontinuidad) > 5 else ''}")

    print("\nGenerando gráfica de la función...")
    x_vals = np.linspace(a if intervalo else punto - 2, b if intervalo else punto + 2, 1000)
    f_lambda = sp.lambdify(x, funcion, modules=["numpy"])
    y_vals = f_lambda(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {funcion_str}", color='blue')

    if punto is not None:
        plt.axvline(punto, color='red', linestyle="--", label=f"x = {punto}")
        plt.scatter([punto], [valor_funcion], color='red', label="Valor en el punto", zorder=5)

    if intervalo is not None:
        for p in puntos_discontinuidad:
            plt.axvline(p, color='purple', linestyle="--", alpha=0.7)

    plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
    plt.axvline(0, color='black', linewidth=0.8, linestyle="--")
    plt.title(f"Gráfica de {funcion_str}")
    plt.xlabel(variable_str)
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


# Ejemplo de uso
estudiar_continuidad("Piecewise((x**2 + 5, x < 2), (1/2, x == 2), (3 + x**3, x > 2))", "x", punto=2)

