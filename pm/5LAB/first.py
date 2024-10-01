import sympy as sp

# Оголошення змінної
x = sp.symbols('x')

# Перша границя
expr1 = (sp.tan(3*x) + sp.tan(x) - sp.sin(2*x)) / (sp.sin(x) - sp.sin(5*x))

# Друга границя
expr2 = (3**(x+1) - 3) / sp.log(1 + x * sp.sqrt(1 + x * sp.exp(x)))

# Обчислення границь
limit_expr1 = sp.limit(expr1, x, 0)
limit_expr2 = sp.limit(expr2, x, 0)

# Виведення результатів
print("Перша границя:", limit_expr1)
print("Друга границя:", limit_expr2)
