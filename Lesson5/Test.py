import unittest
from Homework4.leap import is_year_leap


class TestLeapYear(unittest.TestCase):

    def test_year1987(self):
        self.assertEqual(is_year_leap(1987), False)

    def test_year2024(self):
        self.assertEqual(is_year_leap(2024), True)


if __name__ == '__main':
    unittest.main()
