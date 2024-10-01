import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Визначаємо параметри
n = 100  # Кількість пелюсток
r_max = 5  # Максимальне значення r
theta = np.linspace(0, 2 * np.pi, 1000)  # Кутові координати

# Функція для розрахунку r для даного phi
def rose_curve(phi):
    return r_max * np.cos(n * phi)

# Створюємо фігуру та вісь
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_ylim(0, r_max)

# Перший кадр - промальовування троянди
r = rose_curve(theta)
line, = ax.plot([], [], color='red')

# Функція для ініціалізації
def init():
    line.set_data([], [])
    return line,

# Функція для анімації
def animate(i):
    if i < 100:  # Перші 100 кадрів - проявлення
        line.set_data(theta, r * (i / 100))  # Промальовування
    else:  # Після 100 кадрів - рух
        angle_shift = (i - 100) / 10.0  # Зсув кута
        r_moving = rose_curve(theta + angle_shift)
        line.set_data(theta, r_moving)
    return line,

# Створюємо анімацію
ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, blit=True, interval=50)

plt.show()
