import sympy as sp

# Оголошення параметра t
t = sp.symbols('t')

# Параметричні рівняння
x_param = t**2 / (1 + t**2)
y_param = t / (1 + t**2)

# Перша похідна: dy/dt та dx/dt
dy_dt = sp.diff(y_param, t)
dx_dt = sp.diff(x_param, t)

# Перша похідна dy/dx = (dy/dt) / (dx/dt)
dy_dx = dy_dt / dx_dt

# Друга похідна d²y/dx²
d2y_dx2 = sp.diff(dy_dx, t) / dx_dt

# Спрощення результатів
dy_dx_simplified = sp.simplify(dy_dx)
d2y_dx2_simplified = sp.simplify(d2y_dx2)

# Виведення результатів
print("Перша похідна dy/dx:", dy_dx_simplified)
print("Друга похідна d²y/dx²:", d2y_dx2_simplified)
