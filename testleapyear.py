import unittest
from doofweek import is_leapyear

class TestLeapYear(unittest.TestCase):

    def test_1800_not_leap(self):
            """1800 is NOT a leap year."""
            self.assertFalse(is_leapyear(1800))

    def test_1900_not_leap(self):
            """1900 is NOT a leap year."""
            self.assertFalse(is_leapyear(1900))

    def test_2000_is_leap(self):
            """1800 is NOT a leap year."""
            self.assertTrue(is_leapyear(2000))

    def test_2400_is_leap(self):
            """1800 is NOT a leap year."""
            self.assertTrue(is_leapyear(2400))

if __name__ == '__main__':
    unittest.main()