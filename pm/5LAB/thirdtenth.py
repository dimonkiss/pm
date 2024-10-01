import sympy as sp
from sympy.plotting import plot3d

# Визначення символів
x, y = sp.symbols('x y')

# Визначення рівняння
z_expr = (3*x**2 + 4*y**2 - 8*y + 12) / 4

# Візуалізація 3D графіка
plot3d(z_expr, (x, -2, 2), (y, -2, 2), title='Поверхня: z = (3*x^2 + 4*y^2 - 8*y + 12) / 4', xlabel='Ось X', ylabel='Ось Y', zlabel='Ось Z')
