import matplotlib.pyplot as plt  # Імпорт бібліотеки для побудови графіків
import numpy as np  # Імпорт бібліотеки для роботи з масивами та математичними функціями

num_bins = 21  # Визначаємо кількість випадкових значень (бінів)
values = np.random.randint(1, 100, size=num_bins)  # Генеруємо випадкові значення для гістограми в діапазоні від 1 до 100

bin_edges = [0, 20, 40, 60, 80, 100]  # Визначаємо межі бінів для гістограми
plt.figure(figsize=(10, 6))  # Встановлюємо розмір фігури (ширина, висота)

# Створюємо гістограму з новими кольорами та стилем
plt.hist(values, bins=bin_edges, edgecolor='darkblue', alpha=0.9, color='lightcoral')

plt.xlabel('Значення')  # Підписуємо вісь x
plt.ylabel('Частота')  # Підписуємо вісь y
plt.title('Гістограма з угрупуванням')  # Заголовок гістограми

# Додаємо сітку для кращої читабельності
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()  # Відображаємо побудований графік
