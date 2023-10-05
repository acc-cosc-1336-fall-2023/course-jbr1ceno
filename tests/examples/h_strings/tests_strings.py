import unittest

from src.examples.h_strings.strings import concat_strings, search_in_string, slice_string, slice_w_step_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual(concat_strings("abc", "def"), "abcdef")
        self.assertAlmostEqual("abc" + "def", "abcdef")

    def test_slice_string(self):
        name = "Patty Lynn Smith"
        self.assertEqual(slice_string(name), "Lynn")
        self.assertEqual(name[11:], "Smith")

    def test_slice_w_step(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(slice_w_step_value(letters), "ACEGIKMOQSUWY")

    def test_compare_strings(self):
        #Python compare ASCII numerical values in string comparisons
        str1 = "c" #99
        str2 = "p" #112

        self.assertEqual(str1 < str2, True)
        self.assertEqual(str2 < str1, False)
        self.assertEqual("C++" == "C++ ", False)

    def test_search_in_string(self):
        str1 = "abc"
        str2 = "abcdef"

        self.assertEqual(search_in_string(str1, str2), True)
        self.assertEqual(search_in_string("efg", str2), False)

    def test_is_string_digit(self):
        str1 = "1200"
        self.assertEqual(str1.isdigit(), True)
        self.assertEqual("ab".isdigit(), False)

    def test_string_is_alpha(self):
        str1 = "abcdefg"
        self.assertEqual(str1.isalpha(), True)
        self.assertEqual("$%1".isalpha(), False)

    def test_string_is_upper(self):
        str1 = "XYZ"
        self.assertEqual(str1.isupper(), True)

    def test_string_to_lower(self):
        str1 = "aBcDeF"
        self.assertEqual(str1.lower(), "abcdef")

    def test_string_to_upper(self):
        str1 = "aBcDeF"
        self.assertEqual(str1.upper(), "ABCDEF")

    def test_strip_char_from_strings(self): #gets rid of char from left and right
        str1 = "eeabcdefegfee"
        self.assertEqual(str1.strip("e"), "abcdefegf")

    def test_lstrip_char_from_strings(self):
        str1 = "aaaaxyz"
        self.assertEqual(str1.lstrip("a"), "xyz")

    def self_rstrip_char_from_strings(self):
        str1 = "abcyyy"
        self.assertEqual(str1.rstrip("y"), "abc")

    def test_replace_from_string(self):
        str1 = "eeabcdefegfee"
        self.assertEqual(str1.replace("e", ""), "abcdfgf")

    