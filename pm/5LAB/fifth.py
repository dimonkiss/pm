import sympy as sp

# Оголошення змінних
x, y, z = sp.symbols('x y z')

# Визначення функції u
u = sp.atan(1 / (x * y**2 * z))

# Визначення точки M1
M1 = {x: 1, y: -1, z: 2}

# Обчислення градієнта функції u
grad_u = [sp.diff(u, var) for var in [x, y, z]]

# Оцінка градієнта в точці M1
grad_u_at_M1 = [g.subs(M1) for g in grad_u]

# Обчислення напрямної похідної
directional_derivative = sum(g * d for g, d in zip(grad_u_at_M1, [1, 1, 1]))  # якщо градієнт у напрямку (1, 1, 1)

# Виведення результатів
print("Градієнт в точці M1:", grad_u_at_M1)
print("Напрямна похідна в напрямку градієнта:", directional_derivative)
