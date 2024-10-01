import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Оголошуємо символи
x = sp.symbols('x')
y = sp.Function('y')(x)

# Задане диференціальне рівняння
diff_eq = sp.Eq(y.diff(x, x) + y.diff(x) - 2 * y, sp.exp(2 * x) * sp.sin(x))

# Знайдемо загальний розв'язок
general_solution = sp.dsolve(diff_eq, y)
print("Загальний розв'язок:")
sp.pprint(general_solution)

# Визначимо константи
C1, C2 = sp.symbols('C1 C2')

# Параметри початкових умов
x_val = 0
y_val = -5
y_prime_val = 1

# Розв'язуємо систему для знаходження констант
constants = sp.solve(
    (general_solution.rhs.subs(x, x_val) - y_val,
     general_solution.rhs.diff(x).subs(x, x_val) - y_prime_val),
    (C1, C2)
)

# Знайдемо частковий розв'язок
particular_solution = general_solution.subs({C1: constants[C1], C2: constants[C2]})
print("\nЧастковий розв'язок:")
sp.pprint(particular_solution)

# Побудова графіка часткового розв'язку
x_values = np.linspace(0, 2 * np.pi, 400)
y_values = [particular_solution.rhs.subs(x, val).evalf() for val in x_values]

plt.figure()
plt.plot(x_values, y_values, label='Частковий розв\'язок $y_p(x)$', color='blue')
plt.title('Графік часткового розв\'язку')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()  # Відображення графіка в окремому вікні
