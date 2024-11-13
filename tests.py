import unittest
import math
from circle import area as circle_area
from circle import perimeter as circle_perimeter
from square import area as square_area
from square import perimeter as square_perimeter

class TestCircle(unittest.TestCase):
    """
    Набор тестов для функций, связанных с кругом.
    """

    def test_circle_area(self):
        """
        Тест функции вычисления площади круга.
        Проверяем правильность вычислений для радиусов: 1, 0, 5.
        """
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(5), math.pi * 25)

    def test_circle_perimeter(self):
        """
        Тест функции вычисления длины окружности.
        Проверяем правильность вычислений для радиусов: 1, 0, 5.
        """
        self.assertEqual(circle_perimeter(1), 2 * math.pi)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertEqual(circle_perimeter(5), 2 * math.pi * 5)


class TestSquare(unittest.TestCase):
    """
    Набор тестов для функций, связанных с квадратом.
    """

    def test_square_area(self):
        """
        Тест функции вычисления площади квадрата.
        Проверяем правильность вычислений для сторон: 1, 0, 5.
        """
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(5), 25)

    def test_square_perimeter(self):
        """
        Тест функции вычисления периметра квадрата.
        Проверяем правильность вычислений для сторон: 1, 0, 5.
        """
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(5), 20)

if __name__ == '__main__':
    unittest.main()