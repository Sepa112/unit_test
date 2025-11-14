import unittest
from age import categorize_byAge

class TestAgeCategoriztaion(unittest.TestCase):
    def test_child_category(self):
        self.assertEqual(categorize_byAge(5), "Child")
        self.assertEqual(categorize_byAge(9), "Child")
    def test_teenager_category(self):
        self.assertEqual(categorize_byAge(18), "Teenager")
    def test_adult_category(self):
        self.assertEqual(categorize_byAge(25), "Adult")
    def test_goldenage_category(self):
        self.assertEqual(categorize_byAge(100), "Golden Age")
# python -m unittest .\test_age.py -v