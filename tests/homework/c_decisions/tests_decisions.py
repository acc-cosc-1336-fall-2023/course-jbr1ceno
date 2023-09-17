import unittest

from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio
#from src.homework.c_decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertEqual(.25, get_options_ratio(5, 20))
        self.assertEqual(.5, get_options_ratio(10, 20))

    def test_get_faculty_rating(self):
        self.assertEqual("Unacceptable", get_faculty_rating(.25))
        self.assertEqual("Unacceptable", get_faculty_rating(.5))
        