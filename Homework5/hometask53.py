import unittest
from func_for_53 import is_year_leap
from func_for_53 import is_triangle
from func_for_53 import kind_triangle


class TestFunctions(unittest.TestCase):

    def test_year_1987(self):
        self.assertEqual(is_year_leap(1987), False)

    def test_year_2024(self):
        self.assertEqual(is_year_leap(2024), True)

    def test_year_2000(self):
        self.assertEqual(is_year_leap(2000), False)

    def test_triangle_exist_000(self):
        self.assertEqual(is_triangle(0, 0, 0), False)

    def test_triangle_exist_110(self):
        self.assertEqual(is_triangle(1, 1, 0), False)

    def test_triangle_exist_111(self):
        self.assertEqual(is_triangle(1, 1, 1), True)

    def test_type_of_triangle_000(self):
        self.assertEqual(kind_triangle(0, 0, 0), "Not a triangle")

    def test_type_of_triangle_555(self):
        self.assertEqual(kind_triangle(5, 5, 5), "Equilateral triangle")

    def test_type_of_triangle_662(self):
        self.assertEqual(kind_triangle(6, 6, 2), "Isosceles triangle")

    def test_type_of_triangle_000(self):
        self.assertEqual(kind_triangle(2, 3, 4), "Versatile triangle")


if __name__ == '__main':
    unittest.main()
