import numpy as np
import matplotlib.pyplot as plt

def plot_surface():
    # Створення сітки значень x і y
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Обчислення Z з рівняння
    Z1 = (3 * X**2 + 4 * Y**2 - 8 * Y + 12) / 4  # Відповідь для z (позитивний корінь)
    Z2 = -(3 * X**2 + 4 * Y**2 - 8 * Y + 12) / 4  # Відповідь для z (негативний корінь)

    # Створення графіку
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Побудова кольорових поверхонь
    ax.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.6)
    ax.plot_surface(X, Y, Z2, cmap='plasma', alpha=0.6)

    # Налаштування графіку
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Поверхня: $3x^{2} + 4y^{2} - 4z^{2} - 8y + 8z - 12 = 0$')

    # Показати графік
    plt.show()

# Виклик функції для побудови поверхні
plot_surface()
