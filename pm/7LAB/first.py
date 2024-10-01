import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функцій
def curve1(y):
    return 4 - y**2

def curve2(y):
    return y**2 - 2*y

# Параметри для графіка
y = np.linspace(-20, 40, 800)  # Розширені межі в 10 разів

# Обчислення значень x для обох кривих
x1 = curve1(y)
x2 = curve2(y)

# Створення графіка
plt.figure(figsize=(10, 6))

# Графік для першої кривої (y^2 = 4 - x)
plt.plot(x1, y, color='blue', label='$y^2 = 4 - x$')

# Графік для другої кривої (x = y^2 - 2y)
plt.plot(x2, y, color='red', label='$x = y^2 - 2y$')

# Заливка області між кривими
plt.fill_betweenx(y, np.maximum(x1, x2), np.minimum(x1, x2), where=(x1 > x2), color='lightgray', alpha=0.5)

# Параметри графіка
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.xlim(-40, 50)  # Розширені межі по осі x
plt.ylim(-20, 40)  # Розширені межі по осі y
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки кривих з заливкою внутрішньої області')
plt.legend()
plt.grid()

# Обчислення площі між кривими
y_lower = -2  # Нижня межа (можна змінити в залежності від графіків)
y_upper = 4   # Верхня межа (можна змінити в залежності від графіків)
area, _ = quad(lambda y: curve1(y) - curve2(y), y_lower, y_upper)

print(f"Площа фігури, обмеженої кривими: {abs(area):.2f}")

plt.show()
