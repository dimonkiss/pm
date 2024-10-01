import sympy as sp

# Оголошення змінної
x = sp.symbols('x')

# Інтеграл
integrand = 1 / (x**2 + 4*x + 25)

# Виділення повного квадрата: x^2 + 4x + 25 = (x + 2)^2 + 21
denominator = (x + 2)**2 + 21

# Обчислення невизначеного інтегралу
integral = sp.integrate(1 / denominator, x)

# Виведення результату
print("Інтеграл:", integral)
