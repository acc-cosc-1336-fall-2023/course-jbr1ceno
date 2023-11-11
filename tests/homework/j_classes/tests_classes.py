import unittest

from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):

    def test_get_roll_number(self):
        roll_number = die()
        roll_number.roll()
        roll_number.get_rolled_value()

        print(roll_number.get_rolled_value())
        #self.assertEqual(roll_number.get_rolled_value())