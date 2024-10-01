import sympy as sp

# Визначення параметра t
t = sp.symbols('t')

# Визначення параметричних рівнянь
x = sp.log(t, 2) + t**2
y = sp.sin(sp.pi * t)

# Побудова графіка
sp.plot_parametric(x, y, (t, 0.1, 5), title='Параметрично задана крива',
                   xlabel='x', ylabel='y', show=True)
