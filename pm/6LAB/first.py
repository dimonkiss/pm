import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

# Задаємо диференційне рівняння
diff_eq = sp.Eq(sp.diff(y, x, 2) + 2 * sp.diff(y, x) + y, sp.exp(-x) + sp.sin(x))

# Знаходимо розв'язок
solution = sp.dsolve(diff_eq, y)

# Виводимо розв'язок
sp.pprint(solution)
