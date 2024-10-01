import sympy as sp

# Визначення змінної
x = sp.symbols('x')

# Визначення функції
y = 8 / (x**2 - 4)

# Обчислення похідної
dy_dx = sp.diff(y, x)

# Знаходження критичних точок
critical_points = sp.solve(dy_dx, x)

# Обчислення меж функції при x -> ±2
limits_at_2 = [sp.limit(y, x, 2, dir='+'), sp.limit(y, x, 2, dir='-')]
limits_at_minus_2 = [sp.limit(y, x, -2, dir='+'), sp.limit(y, x, -2, dir='-')]

# Обчислення значення функції в критичних точках
critical_values = [(cp, y.subs(x, cp).evalf()) for cp in critical_points]

# Виведення результатів
print(f"Межі при x -> 2: {limits_at_2}")
print(f"Межі при x -> -2: {limits_at_minus_2}")
print(f"Критичні точки: {critical_points}")
print(f"Значення в критичних точках: {critical_values}")
print(f"Похідна функції: {dy_dx}")

# Побудова графіка
sp.plot(y, (x, -10, 10), title='Графік функції y = 8 / (x^2 - 4)',
         ylabel='y', xlabel='x', ylim=(-10, 10), show=True)
