import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції в полярних координатах
def r(phi):
    return np.cos(phi) + np.sin(phi)

# Обчислення площі
def area(phi):
    return 0.5 * r(phi)**2

# Межі інтегрування
alpha = 0       # Нижня межа
beta = 2 * np.pi  # Верхня межа (один повний оберт)

# Обчислення площі фігури
A, _ = quad(area, alpha, beta)
print(f"Площа фігури, обмеженої кривою: {A:.2f}")

# Побудова графіка
phi = np.linspace(alpha, beta, 400)
r_values = r(phi)

plt.figure(figsize=(8, 8))
plt.polar(phi, r_values, label=r'$r = \cos(\phi) + \sin(\phi)$')  # Додано r перед рядком
plt.title('Графік у полярних координатах')
plt.legend()
plt.grid(True)

plt.show()
