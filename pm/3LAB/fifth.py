import numpy as np
import matplotlib.pyplot as plt


def plot_bar_charts():
    # Кількість стовпчиків
    num_bars = 20
    # Випадкові висоти стовпчиків
    heights1 = np.random.rand(num_bars) * 10
    heights2 = np.random.rand(num_bars) * 10
    heights3 = np.random.rand(num_bars) * 10

    # Позиції стовпчиків по осі x
    x = np.arange(num_bars)

    # Створення графіку
    fig = plt.figure(figsize=(12, 8))

    # Перша діаграма (y = 0)
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.bar(x, heights1, zs=0, zdir='y', alpha=0.8, color=np.random.rand(num_bars, 3))
    ax1.set_title('Діаграма 1 (y = 0)')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Висота')

    # Друга діаграма (y = 3)
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.bar(x, heights2, zs=3, zdir='y', alpha=0.8, color=np.random.rand(num_bars, 3))
    ax2.set_title('Діаграма 2 (y = 3)')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Висота')

    # Третя діаграма (y змінюється від 0.05 до 1)
    y_positions = np.linspace(0.05, 1, num_bars)
    ax3 = fig.add_subplot(133, projection='3d')
    ax3.bar(x, heights3, zs=y_positions, zdir='y', alpha=0.8, color=np.random.rand(num_bars, 3))
    ax3.set_title('Діаграма 3 (y = 0.05 до 1)')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Висота')

    # Показати графік
    plt.tight_layout()
    plt.show()

# Виклик функції для побудови стовпчикових діаграм
plot_bar_charts()
