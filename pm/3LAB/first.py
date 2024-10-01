import matplotlib.pyplot as plt
import numpy as np

def plot_shape(shape):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if shape == 'півколо':
        # Параметри півкола
        radius = 1
        theta = np.linspace(0, np.pi, 100)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        z = np.zeros_like(x)
        ax.plot(x, y, z, color='b', label='Півколо')

    elif shape == 'стрілка':
        # Параметри стрілки
        ax.quiver(0, 0, 0, 1, 1, 0, color='r', label='Стрілка', arrow_length_ratio=0.1)

    elif shape == 'трикутник':
        # Параметри трикутника
        triangle = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3)/2, 0], [0, 0, 0]])
        ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], color='g', label='Трикутник')

    elif shape == 'сектор':
        # Параметри сектора
        radius = 1
        theta = np.linspace(0, np.pi/2, 100)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        z = np.zeros_like(x)
        ax.plot(x, y, z, color='c', label='Сектор')

    elif shape == 'ромб':
        # Параметри ромба
        rhombus = np.array([[0, 1, 0], [1, 0, 0], [0, -1, 0], [-1, 0, 0], [0, 1, 0]])
        ax.plot(rhombus[:, 0], rhombus[:, 1], rhombus[:, 2], color='m', label='Ромб')

    elif shape == 'прямокутник':
        # Параметри прямокутника
        rectangle = np.array([[0, 0, 0], [2, 0, 0], [2, 1, 0], [0, 1, 0], [0, 0, 0]])
        ax.plot(rectangle[:, 0], rectangle[:, 1], rectangle[:, 2], color='y', label='Прямокутник')

    # Налаштування графіку
    ax.set_xlabel('X ось')
    ax.set_ylabel('Y ось')
    ax.set_zlabel('Z ось')
    ax.set_title(f'Фігура: {shape}')
    ax.legend()

    # Показати графік
    plt.show()

# Меню для вибору фігури
shapes = ['півколо', 'стрілка', 'трикутник', 'сектор', 'ромб', 'прямокутник']
print("Оберіть фігуру:")
for i, shape in enumerate(shapes, 1):
    print(f"{i}. {shape}")

choice = int(input("Введіть номер фігури: ")) - 1

if 0 <= choice < len(shapes):
    plot_shape(shapes[choice])
else:
    print("Невірний вибір.")
