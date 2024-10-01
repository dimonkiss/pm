import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Визначення змінної
x = sp.symbols('x')

# Визначення кусочної функції f(x)
f = sp.Piecewise((3*x + 2, x < 0), (0, x >= 0))

# Обчислення коефіцієнтів Фур'є
L = sp.pi
a0 = (1/(2*L)) * sp.integrate(f, (x, -L, L))

n_terms = 10  # Кількість членів ряду Фур'є
an = [(1/L) * sp.integrate(f * sp.cos(n * x / L), (x, -L, L)) for n in range(1, n_terms + 1)]
bn = [(1/L) * sp.integrate(f * sp.sin(n * x / L), (x, -L, L)) for n in range(1, n_terms + 1)]

# Побудова ряду Фур'є
fourier_series = a0 + sum(an[n-1] * sp.cos(n * x / L) + bn[n-1] * sp.sin(n * x / L) for n in range(1, n_terms + 1))

# Генерація значень x для побудови графіка
x_vals = np.linspace(-np.pi, np.pi, 400)
# Генерація значень кусочної функції
f_vals = np.piecewise(x_vals, [x_vals < 0, x_vals >= 0], [lambda x: 3*x + 2, 0])

# Обчислення значень ряду Фур'є
fourier_vals = [fourier_series.evalf(subs={x: val}) for val in x_vals]

# Побудова графіків
plt.figure(figsize=(12, 6))
plt.plot(x_vals, f_vals, label='Кусочна функція f(x)', color='red', linestyle='--')
plt.plot(x_vals, fourier_vals, label='Приблизна функція ряду Фур\'є', color='blue')
plt.title('Приблизна функція ряду Фур\'є для кусочної функції')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
