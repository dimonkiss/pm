import numpy as np
import matplotlib.pyplot as plt


def plot_surface():
    a = 1
    u = np.linspace(-5, 5, 100)
    v = np.linspace(-5, 5, 100)
    U, V = np.meshgrid(u, v)
    R = (a / 2) * (np.exp(U / 2) + np.exp(-U / 2))
    X = R * np.cos(U)
    Y = R * np.sin(U)
    Z = V
    return X, Y, Z

def plot_scatter():
    x = np.linspace(-5, 5, 20)
    y = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x, y)
    Z1 = (3 * X**2 + 4 * Y**2 - 8 * Y + 12) / 4
    Z2 = -(3 * X**2 + 4 * Y**2 - 8 * Y + 12) / 4
    return X, Y, Z1, Z2

def plot_polar_contour():
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.linspace(0, 5, 100)
    R, T = np.meshgrid(r, theta)
    X = R * np.cos(T)
    Y = R * np.sin(T)
    Z = np.sin(R)
    return X, Y, Z

def plot_polar_curve(ax):
    alpha = np.linspace(0, 2 * np.pi, 500)
    p = 0.5 / (1 + 0.5 * np.cos(alpha))
    ax.plot(np.cos(alpha) * p, np.sin(alpha) * p, color='white', label=r'$p = \frac{0.5}{1+0.5\cdot \cos(\alpha)}$')
    ax.set_title('Крива другого порядку в полярних координатах')
    ax.legend()

# Створення загального графічного вікна
fig = plt.figure(figsize=(15, 10))

# Перша діаграма: Каркасний графік поверхні
X, Y, Z = plot_surface()
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax1.set_title('Каркасний графік поверхні')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Друга діаграма: Розсіяний графік поверхні
X, Y, Z1, Z2 = plot_scatter()
ax2 = fig.add_subplot(223, projection='3d')
ax2.scatter(X, Y, Z1, c='blue', label='Позитивний корінь', alpha=0.6)
ax2.scatter(X, Y, Z2, c='red', label='Негативний корінь', alpha=0.6)
ax2.set_title('Розсіяний графік поверхні')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.legend()

# Третя діаграма: Залитий контурний графік з накладеною полярною кривою
ax3 = fig.add_subplot(224)
X, Y, Z = plot_polar_contour()
contour_filled = ax3.contourf(X, Y, Z, levels=20, cmap='viridis')
ax3.set_title('Залитий контурний графік')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.contour(X, Y, Z, levels=20, colors='black')

# Накласти полярну криву
plot_polar_curve(ax3)

# Налаштування макету
plt.tight_layout()
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
