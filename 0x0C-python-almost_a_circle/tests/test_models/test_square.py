#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Square._Square__nb_objects = 0

    def tearDown(self):
        pass

    def test_sq_id1(self):
        self.a0 = Square(10, 3)
        self.a3 = Square(10, 2, 9, 12)
        self.assertEqual(self.a3.id, 12)

    def test_sq_area(self):
        self.a0 = Square(91)
        self.assertEqual(self.a0.area(), 8281)

    def test_sq_noargs(self):
        try:
            self.a0 = Rectangle()

        except:
            self.assertRaises(TypeError, "__init__() missing 1 required positional argument: 'size'")

    def test_sq_wrong_size(self):
        try:
            self.a0 = Square("9")

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_wrong_size2(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Square(None)

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_wrong_size3(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Square([])

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_bad_size4(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.a1 = Square(-9)

    def test_sq_bad_size5(self):
        try:
            self.a0 = Square((1, 9))

        except:
            self.assertRaises(TypeError, "width must be an integer")

    def test_sq_bad_x(self):
            with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                self.a0 = Square(1, -9, 1)

    def test_sq_bad_y(self):
            with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                self.a0 = Square(1, 2, -9)
