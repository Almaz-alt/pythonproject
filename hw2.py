# Базовый класс Figure
class Figure:
    # Атрибут уровня класса
    unit = "cm"

    # Конструктор без атрибутов уровня объекта
    def __init__(self):
        pass

    # Нереализованный метод для подсчета площади
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть реализован в подклассах")

    # Нереализованный метод для вывода информации о фигуре
    def info(self):
        raise NotImplementedError("Метод info должен быть реализован в подклассах")


# Класс Square, наследуемый от Figure
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # Приватный атрибут

    # Переопределение метода calculate_area
    def calculate_area(self):
        return self.__side_length ** 2

    # Переопределение метода info
    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}")


# Класс Rectangle, наследуемый от Figure
class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # Приватный атрибут
        self.__width = width  # Приватный атрибут

    # Переопределение метода calculate_area
    def calculate_area(self):
        return self.__length * self.__width

    # Переопределение метода info
    def info(self):
        area = self.calculate_area()
        print(
            f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}")


# Исполняемая часть программы
if __name__ == "__main__":
    # Создаем список фигур
    shapes = [
        Square(5),
        Square(10),
        Rectangle(5, 8),
        Rectangle(10, 15),
        Rectangle(20, 25)
    ]

    # Вызываем метод info для каждой фигуры
    for shape in shapes:
        shape.info()