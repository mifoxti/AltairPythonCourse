from math import pi

class Shape:
    """Абстрактный базовый класс Фигура"""

    def area(self):
        """Абстрактный метод - должен быть реализован в потомках"""
        raise NotImplementedError("Метод area должен быть переопределен в дочернем классе")

    def perimeter(self):
        """Абстрактный метод"""
        raise NotImplementedError("Метод perimeter должен быть переопределен в дочернем классе")

    def __str__(self):
        """Магический метод для красивого вывода"""
        return f"{self.__class__.__name__}: площадь: {self.area()}, периметр: {self.perimeter()}"

class Rectangle(Shape):
    """Класс Прямоугольник"""

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        """Реализация абстрактного метода"""
        return self._length * self._width

    def perimeter(self):
        """Реализация абстрактного метода"""
        return 2 * (self._length + self._width)

    def is_square(self):
        """Проверка, является ли прямоугольник квадратом"""
        return self._length == self._width


class Circle(Shape):
    """Класс Круг"""

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        """Своя реализация метода are"""
        return pi * (self._radius ** 2)

    def perimeter(self):
        """Своя реализация метода perimetr"""
        return 2 * self._radius * self._radius

    def diameter(self):
        """Специфичный метод для круга"""
        return 2 * self._radius

class Triangle(Shape):
    """Класс Треугольник"""

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def area(self):
        """Формула Герона для площади треугольника"""
        s = self.perimeter() / 2
        return (s * (s - self._a) * (s - self._b) * (s - self._c)) ** 0.5

    def perimeter(self):
        """Периметр треугольника"""
        return self._a + self._b + self._c

    def is_equilateral(self):
        """Проверка на равносторонность"""
        return self._a == self._b == self._c


def process_shapes(shapes):
    """
    Эта функция работает с любыми объектами, у которых есть методы area() и perimeter()
    Она не знает и не должна знать о конкретных типах фигур
    """
    total_area = 0
    total_perimeter = 0

    print("=== ОБРАБОТКА ФИГУР ===")
    for shape in shapes:
        # Полиморфизм в действии: один интерфейс и разное поведение
        area = shape.area()
        perimeter = shape.perimeter()

        total_area += area
        total_perimeter += perimeter

        print(f"{shape}")

    print(f"\n📊 Суммарная площадь: {total_area:.2f}")
    print(f"📊 Суммарный периметр: {total_perimeter:.2f}")


shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5),
    Rectangle(2, 2),
    Circle(2.5)
]

process_shapes(shapes)

# Дополнительная демонстрация работы специфических методов
print("\n=== СПЕЦИФИЧНЫЕ МЕТОДЫ ===")
for shape in shapes:
    if isinstance(shape, Rectangle):
        print(f"Прямоугольник - квадрат: {shape.is_square()}")
    elif isinstance(shape, Circle):
        print(f"Круг - диаметр: {shape.diameter()}")
    elif isinstance(shape, Triangle):
        print(f"Треугольник - равносторонний: {shape.is_equilateral()}")




































