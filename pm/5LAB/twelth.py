import sympy as sp

# Визначення змінних
x, y = sp.symbols('x y')

# Неявні рівняння
eq1 = sp.Eq(25*x**2 + 4*y**2 - 100, 0)  # Крива 1
eq2 = sp.Eq(y - 2, (-9/5) * sp.sqrt(25 + x**2))  # Крива 2

# Побудова графіка для першої кривої
p1 = sp.plot_implicit(eq1, (x, -100, 100), (y, -100, 100), line_color='blue', show=False)

# Побудова графіка для другої кривої
p2 = sp.plot_implicit(eq2, (x, -100, 100), (y, -100, 100), line_color='red', show=False)

# Об'єднати графіки
p1.extend(p2)

# Відобразити об'єднаний графік
p1.title = 'Неявно задані криві'
p1.show()
