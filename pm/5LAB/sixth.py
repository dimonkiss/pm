import sympy as sp

# Оголошення змінних
x, y = sp.symbols('x y')

# Визначення функції f(x, y)
f = (x**2 / y**3) - 2*x - (1/y) - 2*y - 2

# Обчислення часткових похідних
f_x = sp.diff(f, x)  # Часткова похідна за x
f_y = sp.diff(f, y)  # Часткова похідна за y

# Знаходження критичних точок
critical_points = sp.solve([f_x, f_y], (x, y))

# Обчислення других часткових похідних
f_xx = sp.diff(f_x, x)  # Друга часткова похідна за x
f_yy = sp.diff(f_y, y)  # Друга часткова похідна за y
f_xy = sp.diff(f_x, y)  # Змішана часткова похідна

# Тест другого похідного в критичних точках
second_derivative_results = []
for point in critical_points:
    D = f_xx.subs({x: point[0], y: point[1]}) * f_yy.subs({x: point[0], y: point[1]}) - f_xy.subs({x: point[0], y: point[1]})**2
    second_derivative_results.append((point, D))

# Виведення результатів
print("Критичні точки:", critical_points)
print("Результати другого похідного тесту:", second_derivative_results)
