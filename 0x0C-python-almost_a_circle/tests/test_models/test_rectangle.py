#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Rectangle._Rectangle__nb_objects = 0

    def tearDown(self):
        pass

    def test_rect_id1(self):
        self.a0 = Rectangle(10, 3)
        self.a3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.a3.id, 12)

    def test_rect_noargs(self):
        try:
            self.a0 = Rectangle()

        except:
            self.assertRaises(TypeError, "__init__() missing 2 required positional arguments: 'width' and 'height'")

    def test_rect_one_arg(self):
        try:
            self.a9 = Rectangle(1)

        except:
            self.assertRaises(TypeError, "__init__() missing 1 required positional argument: 'height'")

    def test_rect_wrong_width1(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Rectangle(2, "9")

        except:
            self.assertRaises(TypeError, "height must be an integer")

    def test_rect_wrong_width2(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Rectangle(2, None)

        except:
            self.assertRaises(TypeError, "height must be an integer")

    def test_rect_wrong_width3(self):
        try:
            self.a0 = Rectangle(1, 2)
            self.a1 = Rectangle(2, [])

        except:
            self.assertRaises(TypeError, "height must be an integer")

    def test_rect_bad_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.a1 = Rectangle(0, 9)

    def test_rect_bad_height(self):
         with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.a0 = Rectangle(1, -9)

    def test_rect_bad_x(self):
            with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                self.a0 = Rectangle(1, 2, -9, 1)

    def test_rect_bad_y(self):
            with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                self.a0 = Rectangle(1, 2, 9, -1)
