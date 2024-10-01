import sympy as sp

# Оголосимо символи та функції
t = sp.symbols('t')
x = sp.Function('x')(t)
y = sp.Function('y')(t)

# Система диференціальних рівнянь
eq1 = sp.Eq(sp.Derivative(x, t), -2*x + 5*y + 3)
eq2 = sp.Eq(sp.Derivative(y, t), -x + 2*y - 4)

# Розв'язок системи
result = sp.dsolve((eq1, eq2))

# Вивести розв'язок
print(result)
