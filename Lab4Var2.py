import matplotlib.pyplot as plt

# Определяем функцию для вычисления угла поворота
def orientation(p, q, r):
    """ Возвращает положительное значение, если поворот против часовой стрелки,
        отрицательное значение - по часовой стрелке, и 0 если они коллинеарны.
    """
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

# Функция для построения выпуклой оболочки
def convex_hull(points):
    # Сначала найдем самую нижнюю точку (или самую левую при равенстве Y)
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # Конкатенируем нижнюю и верхнюю цепи для получения полного контура
    return lower[:-1] + upper[:-1]

# Задаем координаты точек
points = [
    (9, -9), 
    (8, -4), 
    (9, 5), 
    (9, 10), 
    (6, 5), 
    (-4, 0), 
    (1, 0)
]

# Получаем выпуклую оболочку
hull = convex_hull(points)

# Визуализация точек и выпуклой оболочки
plt.plot([p[0] for p in points], [p[1] for p in points], 'o')
hull_points = hull + [hull[0]]  # Замыкаем контур
plt.plot([p[0] for p in hull_points], [p[1] for p in hull_points], 'r-')

# Отметим вершины выпуклой оболочки
for p in hull:
    plt.plot(p[0], p[1], 'ro')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Выпуклая оболочка для множества точек')
plt.show()
