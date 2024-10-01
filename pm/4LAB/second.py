import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# Функція для обчислення параметра r
def r(u, a):
    return (a / 2) * (np.exp(u / 2) + np.exp(-u / 2))


# Створюємо фігуру та 3D осі
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Параметри поверхні
a = 1  # Розмір поверхні
u_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)
v_vals = np.linspace(-5, 5, 100)

# Створюємо сітку параметрів u та v
U, V = np.meshgrid(u_vals, v_vals)


# Функція для оновлення кадру
def update(frame):
    ax.clear()  # Очищаємо попередню поверхню

    # Динамічно змінюємо u
    u_dynamic = U + frame * 0.05  # Додаємо зміщення до u

    # Обчислюємо нові значення для r, x, y, z
    R = r(u_dynamic, a)
    X = R * np.cos(u_dynamic)
    Y = R * np.sin(u_dynamic)
    Z = V

    # Малюємо поверхню
    surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

    # Додаємо назви осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Анімація параметричної поверхні')

    # Налаштування меж для осей
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-5, 5])

    return surface,


# Створюємо анімацію
ani = FuncAnimation(fig, update, frames=200, interval=100)

# Відображаємо анімацію
plt.show()
