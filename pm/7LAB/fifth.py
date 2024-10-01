import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Параметричні рівняння
def x(t):
    return 3 * (t - np.sin(t))

def y(t):
    return 3 * (1 - np.cos(t))

# Похідні
def dx_dt(t):
    return 3 * (1 - np.cos(t))

def dy_dt(t):
    return 3 * np.sin(t)

# Функція для довжини кривої
def integrand(t):
    return np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)

# Межі інтегрування
a = np.pi
b = 3 * np.pi

# Обчислення довжини
L, _ = quad(integrand, a, b)
print(f"Довжина лінії: {L:.4f}")

# Побудова графіка
t_values = np.linspace(a, b, 400)
x_values = x(t_values)
y_values = y(t_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$x = 3(t - \sin(t)), y = 3(1 - \cos(t))$', color='blue')
plt.title('Графік параметричної кривої')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.xlim(0, 30)  # Вибір обмеження для x
plt.ylim(-1, 15)  # Вибір обмеження для y
plt.show()
