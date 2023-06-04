import math

# Метод прямоугольников
def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        x = a + i * h
        result += f(x)
    result *= h
    return result

# Метод тrapezoidal
def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        result += f(x)
    result *= h
    return result

# Функция, описывающая часть окружности
def circle_function(x, R):
    return math.sqrt(R**2 - x**2)

# Точное значение длины части окружности
def exact_length(R):
    return math.pi * R / 2

# Параметры окружности
R = 1.0
a = -R / math.sqrt(2)
b = R / math.sqrt(2)

# Количество интервалов
n = 1000

# Вычисление длины части окружности методом прямоугольников
length_rectangle = rectangle_method(lambda x: math.sqrt(1 + (circle_function(x, R))**2), a, b, n)

# Вычисление длины части окружности методом трапеций
length_trapezoidal = trapezoidal_method(lambda x: math.sqrt(1 + (circle_function(x, R))**2), a, b, n)

# Точное значение длины части окружности
exact_length_value = exact_length(R)

# Вывод результатов
print(f"Метод прямоугольников: {length_rectangle}")
print(f"Метод трапеций: {length_trapezoidal}")
print(f"Точное значение: {exact_length_value}")
