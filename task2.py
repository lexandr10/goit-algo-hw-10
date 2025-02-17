import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a, b = 0, 2  # Верхня межа

# Метод Монте-Карло
num_samples = 1000
x_random = np.random.uniform(a,b,num_samples)
y_random = np.random.uniform(0, f(b), num_samples)

under_curve = y_random < f(x_random)
monte_carlo_integral = (under_curve.sum() / num_samples) * (b * f(b))

# Аналітичне обчислення інтегралу
analytical_integral, _ = spi.quad(f, a, b)

print(f"Monte Carlo Integral: {monte_carlo_integral}")
print(f"Analytical Integral: {analytical_integral}")
print(f"Error: {abs(monte_carlo_integral - analytical_integral)}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()



# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
