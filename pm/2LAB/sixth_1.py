import matplotlib.pyplot as plt  # Імпорт бібліотеки для побудови графіків
import numpy as np  # Імпорт бібліотеки для роботи з масивами та математичними функціями

num_bars = 21  # Визначаємо кількість стовпчиків у діаграмі
values = np.random.randint(1, 100, size=num_bars)  # Генеруємо випадкові значення для стовпчиків у діапазоні від 1 до 100

colors = ['red', 'green', 'blue', 'orange']  # Визначаємо кольори для частин стовпчиків
bar_width = 0.4  # Встановлюємо ширину одного стовпчика
bar_positions = np.arange(num_bars)  # Створюємо масив позицій для стовпчиків

# Цикл для створення 4 частин (кольорів) у кожному стовпчику
for i in range(4):
    color_values = values / 4  # Ділимо значення на 4, щоб розподілити їх між 4 кольорами
    # Будуємо стовпчики з певними зміщеннями для кожного кольору
    plt.bar(bar_positions + i * bar_width / 4, color_values, width=bar_width / 4, color=colors[i])

plt.xlabel('Номери стовпців')  # Підписуємо вісь x
plt.ylabel('Значення')  # Підписуємо вісь y
plt.title('Стовпчикова діаграма з 4 кольорами в кожному стовпчику')  # Заголовок діаграми
# Встановлюємо підписи на осі x, відображаючи номери стовпців
plt.xticks(bar_positions + bar_width / 2, range(1, num_bars + 1))
plt.show()  # Відображаємо побудований графік
