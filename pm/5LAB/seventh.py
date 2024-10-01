import sympy as sp

# Визначення комплексного числа
complex_number = 27 * sp.I

# Знаходження модуля та аргументу комплексного числа
r = abs(complex_number)  # модуль
theta = sp.arg(complex_number)  # аргумент

# Обчислення кубічних коренів
roots = [r**(1/3) * sp.exp(sp.I * (theta + 2 * sp.pi * k) / 3) for k in range(3)]

# Виведення результатів
for i, root in enumerate(roots):
    print(f"Корінь {i+1}: {root.simplify()}")
