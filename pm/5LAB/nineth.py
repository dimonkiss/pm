import sympy as sp

# Визначення змінної
n = sp.symbols('n')

# Визначення ряду
series = (7**n - 2**n) / (14**n)

# Обчислення суми ряду
sum_series = sp.Sum(series, (n, 1, sp.oo)).doit()

# Перевірка збіжності за допомогою критерію співвідношення
ratio_test = sp.limit(sp.Abs(series.subs(n, n + 1) / series), n, sp.oo)

# Виведення результатів
print(f"Сума ряду: {sum_series}")
print(f"Значення тесту на збіжність: {ratio_test}")
