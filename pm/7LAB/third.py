import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Параметричні рівняння
def x(t):
    return 10 * (t - np.sin(t))

def y(t):
    return 10 * (1 - np.cos(t))

# Обчислення похідної dx/dt
def dx_dt(t):
    return 10 * (1 - np.cos(t))

# Обчислення y = 15
y_upper = 15

# Знайдемо t, для яких y(t) = 15
# 10(1 - cos(t)) = 15
# cos(t) = -0.5
# t = 2π/3 + 2nπ або 4π/3 + 2nπ (n ∈ Z)
t1 = 2 * np.pi / 3
t2 = 4 * np.pi / 3

# Функція для обчислення площі
def area(t):
    return (y(t) - y_upper) * dx_dt(t)

# Обчислення площі
A, _ = quad(area, t1, t2)
print(f"Площа фігури, обмеженої кривими: {A:.2f}")

# Побудова графіка
t = np.linspace(0, 2 * np.pi, 400)  # Нові межі для графіка
x_values = x(t)
y_values = y(t)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$x = 10(t - \sin(t)), y = 10(1 - \cos(t))$', color='blue')
plt.axhline(y_upper, color='red', linestyle='--', label='$y = 15$')

# Заливка області між кривими (вища лінія)
plt.fill_between(x_values, y_upper, y_values, where=(y_values >= y_upper), color='lightgray', alpha=0.5)

plt.title('Параметричні рівняння і горизонтальна лінія з заливкою')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.xlim(0, 70)  # Можливо, потрібно коригувати в залежності від діапазону
plt.ylim(0, 20)
plt.show()
