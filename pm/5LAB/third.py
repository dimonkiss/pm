import sympy as sp

# Оголошення змінної
x = sp.symbols('x')

# Многочлен
P4_x = 5*x**4 - 3*x**2 - 8

# Розклад на множники
factored_P4_x = sp.factor(P4_x)

# Виведення результату
print("Розклад на множники:", factored_P4_x)
