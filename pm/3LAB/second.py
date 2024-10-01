import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_3d_polygon_with_arrows():
    # Кількість вершин
    num_sides = 16
    # Кут між вершинами
    theta = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    # Координати вершин
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros_like(x)  # Всі точки на площині z=0

    # Створення фігури та осей
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Заповнена кольором фігура
    vertices = np.column_stack((x, y, z))
    polygon = Poly3DCollection([vertices], color='lightblue', alpha=0.5)
    ax.add_collection3d(polygon)

    # Додавання стрілок на контурі
    for i in range(num_sides):
        ax.quiver(x[i], y[i], z[i], x[(i + 1) % num_sides] - x[i], y[(i + 1) % num_sides] - y[i], 0,
                   arrow_length_ratio=0.1, color='orange', linewidth=1.5)

    # Обчислення координат центру
    center_x = np.mean(x)
    center_y = np.mean(y)
    center_z = np.mean(z)

    # Додавання тексту в центрі
    ax.text(center_x, center_y, center_z, '16-багатокутник', horizontalalignment='center',
            verticalalignment='center', fontsize=12, color='black', fontweight='bold')

    # Налаштування графіку
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-0.5, 0.5)  # Висота Z для тексту
    ax.set_aspect('auto')
    ax.axis('off')  # Вимкнення осей
    ax.set_title('16-багатокутник у 3D з контуром та текстом всередині')

    # Показати графік
    plt.show()

# Виклик функції для малювання 16-багатокутника у 3D
plot_3d_polygon_with_arrows()
