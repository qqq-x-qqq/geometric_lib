import unittest
import math

import circle
import square
import rectangle
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_mixed_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("5a", 5)
        with self.assertRaises(TypeError):
            rectangle.perimeter("5a", 5)
    def test_symbol_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("!", 5)
        with self.assertRaises(TypeError):
            rectangle.perimeter("!", 5)
    def test_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(4, -5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(4, -5)
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
    def test_mixed_string(self):
        with self.assertRaises(TypeError):
            circle.area("5a")
        with self.assertRaises(TypeError):
            circle.perimeter("5a")
    def test_symbol_string(self):
        with self.assertRaises(TypeError):
            circle.area("!")
        with self.assertRaises(TypeError):
            circle.perimeter("!")
    def test_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-5)
        with self.assertRaises(ValueError):
            circle.perimeter(-5)
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
    def test_mixed_string(self):
        with self.assertRaises(TypeError):
            square.area("5a")
        with self.assertRaises(TypeError):
            square.perimeter("5a")
    def test_symbol_string(self):
        with self.assertRaises(TypeError):
            square.area("!")
        with self.assertRaises(TypeError):
            square.perimeter("!")
    def test_negative(self):
        with self.assertRaises(ValueError):
            square.area(-5)
        with self.assertRaises(ValueError):
            square.perimeter(-5)
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
    def test_mixed_string(self):
        with self.assertRaises(TypeError):
            triangle.area("5a", 5)
        with self.assertRaises(TypeError):
            triangle.perimeter("5a", 5)
    def test_symbol_string(self):
        with self.assertRaises(TypeError):
            triangle.area("!", 5)
        with self.assertRaises(TypeError):
            triangle.perimeter("!", 5)
    def test_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(4, -5)
        with self.assertRaises(ValueError):
            triangle.perimeter(4, -5)
    def test_zero_mul(self):
        res = triangle.area(10,0)
        self.assertEqual(res, 0)
    def test_triangle_area(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)
    def test_triangle_perimetr(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
