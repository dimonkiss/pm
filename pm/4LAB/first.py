import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Функція для створення параметричної кривої
def parametric_curve(t):
    x = t ** 2 / (1 + t ** 2)
    y = t / (1 + t ** 2)
    return x, y


# Створюємо фігуру та осі для графіка
fig, ax = plt.subplots()
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.6, 0.6)
line, = ax.plot([], [], lw=2)

# Кольори для анімації
colors = ['blue', 'green', 'red']
color_index = 0


# Функція для ініціалізації анімації
def init():
    line.set_data([], [])
    return line,


# Функція для оновлення анімації
def update(frame):
    global color_index
    t = np.linspace(-10, 10, 500)
    x, y = parametric_curve(t)

    # Рух зліва направо: зникає
    if frame < 50:
        visible_range = frame / 50  # Від 0 до 1
        line.set_data(x[:int(visible_range * len(x))], y[:int(visible_range * len(y))])

    # Рух справа наліво: з'являється
    elif frame < 100:
        visible_range = (frame - 50) / 50  # Від 0 до 1
        line.set_data(x[int(visible_range * len(x)):], y[int(visible_range * len(y)):])

    # Після завершення циклу оновлюємо колір
    if frame == 100:
        color_index = (color_index + 1) % len(colors)
        line.set_color(colors[color_index])

    return line,


# Створюємо анімацію на 100 кадрів
ani = FuncAnimation(fig, update, frames=np.arange(0, 101, 1),
                    init_func=init, blit=True, interval=100, repeat=True)

plt.title('Анімація параметричної кривої')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.grid(True)

# Відображення анімації
plt.show()
