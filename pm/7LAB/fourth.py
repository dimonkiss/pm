import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція y
def y(x):
    return (x**3) / 6 + (1/2) * x

# Похідна dy/dx
def dy_dx(x):
    return (x**2) / 2 + (1 / 2)

# Функція для довжини кривої
def integrand(x):
    return np.sqrt(1 + dy_dx(x)**2)

# Межі інтегрування
a = 1
b = 3

# Обчислення довжини
L, _ = quad(integrand, a, b)
print(f"Довжина лінії: {L:.4f}")

# Побудова графіка
x_values = np.linspace(a, b, 400)
y_values = y(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$y = \frac{x^3}{6} + \frac{1}{2}x$', color='blue')
plt.title('Графік функції')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.xlim(0, 4)  # Вибір обмеження для x
plt.ylim(0, 10)  # Вибір обмеження для y
plt.show()
