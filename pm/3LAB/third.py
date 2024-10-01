import numpy as np
import matplotlib.pyplot as plt


def plot_surface():
    # Параметри
    a = 1  # Ви можете змінити це значення за потребою
    u = np.linspace(-5, 5, 100)  # Значення u
    v = np.linspace(-5, 5, 100)  # Значення v
    U, V = np.meshgrid(u, v)

    # Обчислення r
    R = (a / 2) * (np.exp(U / 2) + np.exp(-U / 2))

    # Обчислення координат x, y, z
    X = R * np.cos(U)
    Y = R * np.sin(U)
    Z = V

    # Створення графіку
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Побудова поверхні
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    # Налаштування графіку
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Поверхня: $x = r \cos u, y = r \sin u, z = v, r = \\frac{a}{2} \\left( \\exp \\frac{u}{2} + \\exp \\frac{-u}{2} \\right)$')

    # Показати графік
    plt.show()

# Виклик функції для побудови поверхні
plot_surface()
