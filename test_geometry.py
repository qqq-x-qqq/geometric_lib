import unittest
import math

import circle
import square
import rectangle
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10,0)
        self.assertEqual(res, 0)
    def test_rectangle_area(self):
        res = rectangle.area(4, 5)
        self.assertEqual(res, 20)
    def test_rectangle_perimetr(self):
        res = rectangle.perimeter(4, 5)
        self.assertEqual(res, 18)

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_circle_area(self):
        res = circle.area(5)
        self.assertEqual(res, math.pi*25)
    def test_circle_perimetr(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2*math.pi * 5)

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_square_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)
    def test_square_perimetr(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(10,0)
        self.assertEqual(res, 0)
    def test_triangle_area(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)
    def test_triangle_perimetr(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
