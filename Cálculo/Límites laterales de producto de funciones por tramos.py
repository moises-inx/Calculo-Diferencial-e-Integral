import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir las funciones por tramos usando sympy
f1_sym = sp.Piecewise((x**2 + 1, x <= 1), (x + 3, x > 1))
f2_sym = sp.Piecewise((x - 2, x <= 1), (-1/2, x > 1))
f_prod_sym = f1_sym * f2_sym

# Evaluar los límites laterales en el punto crítico x = 1
punto = 1
lim_f1_left = sp.limit(x**2 + 1, x, punto, dir='-')  # Límite por izquierda de f(x)
lim_f1_right = sp.limit(x + 3, x, punto, dir='+')  # Límite por derecha de f(x)
lim_f2_left = sp.limit(x - 2, x, punto, dir='-')  # Límite por izquierda de g(x)
lim_f2_right = sp.limit(-1/2, x, punto, dir='+')  # Límite por derecha de g(x)
lim_prod_left = sp.limit(lim_f1_left * lim_f2_left, x, punto, dir='-')
lim_prod_right = sp.limit(lim_f1_right * lim_f2_right, x, punto, dir='+')

# Mostrar resultados
print("Evaluación de límites laterales en x = 1:")
print(f"  Límite izquierdo de f(x): {lim_f1_left}")
print(f"  Límite derecho de f(x): {lim_f1_right}")
if lim_f1_left == lim_f1_right:
    print("  El límite de f(x) existe y es:", lim_f1_left)
else:
    print("  El límite de f(x) no existe.")

print(f"  Límite izquierdo de g(x): {lim_f2_left}")
print(f"  Límite derecho de g(x): {lim_f2_right}")
if lim_f2_left == lim_f2_right:
    print("  El límite de g(x) existe y es:", lim_f2_left)
else:
    print("  El límite de g(x) no existe.")

print(f"  Límite izquierdo de f(x) * g(x): {lim_prod_left}")
print(f"  Límite derecho de f(x) * g(x): {lim_prod_right}")
if lim_prod_left == lim_prod_right:
    print("  El límite de f(x) * g(x) existe y es:", lim_prod_left)
else:
    print("  El límite de f(x) * g(x) no existe.")

# Generar los datos para la gráfica
x_vals_left = np.linspace(-1, 1, 200, endpoint=False)  # No incluye x=1
x_vals_right = np.linspace(1, 3, 200)  # Incluye x=1 desde la derecha
x_vals = np.concatenate([x_vals_left, x_vals_right])

f1_np_left = x_vals_left**2 + 1
f1_np_right = x_vals_right + 3
f1_np = np.concatenate([f1_np_left, f1_np_right])

f2_np_left = x_vals_left - 2
f2_np_right = -1/2 * np.ones_like(x_vals_right)
f2_np = np.concatenate([f2_np_left, f2_np_right])

f_prod_np = f1_np * f2_np

# Graficar las funciones por tramos
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_vals_left, f1_np_left, 'b--', label="f(x) para x ≤ 1")
plt.plot(x_vals_right, f1_np_right, 'b--', label="f(x) para x > 1")
plt.plot(x_vals_left, f2_np_left, 'g:', label="g(x) para x ≤ 1")
plt.plot(x_vals_right, f2_np_right, 'g:', label="g(x) para x > 1")
plt.scatter([1], [lim_f1_left], color='red', label="Discontinuidad f(x)")
plt.scatter([1], [lim_f2_left], color='orange', label="Discontinuidad g(x)")
plt.title("Funciones por tramos")
plt.legend()
plt.grid()

# Graficar la multiplicación de las funciones
plt.subplot(1, 2, 2)
plt.plot(x_vals, f_prod_np, 'r-', label="f(x) * g(x)")
plt.scatter([1], [lim_prod_left], color='purple', label="Discontinuidad f(x) * g(x)")
plt.title("Producto de funciones por tramos")
plt.legend()
plt.grid()

plt.show()