import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию и ее производную
def f(x):
    return 2*x**3 - 3*x**2 - 12*x + 1

def f_prime(x):
    return 6*x**2 - 6*x - 12

# Создаем диапазон x
x = np.linspace(-3, 4, 400)
y = f(x)

# Критические точки (где f'(x) = 0)
crit_x = [-1, 2]
crit_y = [f(pt) for pt in crit_x]

# Определяем интервалы знаков производной
test_points = [-2, 0, 3]  # по точке в каждом интервале
signs = []
for pt in test_points:
    signs.append("+" if f_prime(pt) > 0 else "-")

# Строим график
plt.figure(figsize=(12, 8))

# 1. График функции
plt.plot(x, y, 'b-', linewidth=2, label=r'$y = 2x^3 - 3x^2 - 12x + 1$')

# 2. Критические точки
plt.scatter(crit_x, crit_y, color='red', s=100, zorder=5, label='Критические точки')

# 3. Горизонтальные касательные (в критических точках)
for cx, cy in zip(crit_x, crit_y):
    plt.axhline(y=cy, xmin=(cx - x.min())/(x.max() - x.min()) - 0.05,
                xmax=(cx - x.min())/(x.max() - x.min()) + 0.05,
                color='purple', linestyle='--', linewidth=1.5)

# 4. Заливка интервалов возрастания
x_inc1 = np.linspace(-3, -1, 100)
x_inc2 = np.linspace(2, 4, 100)
plt.fill_between(x_inc1, f(x_inc1), alpha=0.2, color='green', label='Возрастание')
plt.fill_between(x_inc2, f(x_inc2), alpha=0.2, color='green')

# 5. Заливка интервала убывания
x_dec = np.linspace(-1, 2, 100)
plt.fill_between(x_dec, f(x_dec), alpha=0.2, color='orange', label='Убывание')

# 6. Подписи критических точек
plt.text(-1, f(-1) - 3, r'$x = -1$ (макс)', ha='center', fontsize=11, color='darkred')
plt.text(2, f(2) + 2, r'$x = 2$ (мин)', ha='center', fontsize=11, color='darkred')

# 7. Сетка и оформление
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('График функции с интервалами возрастания/убывания', fontsize=14)
plt.legend(loc='upper left', fontsize=11)
plt.ylim(-25, 20)

plt.tight_layout()
plt.show()
