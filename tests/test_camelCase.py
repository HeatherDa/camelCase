import unittest
from camelCase_Converter import camelCase
from camelCase_Converter.camelCase import CamelError

class TestCamelCase(unittest.TestCase):
    def test_camelCase(self):
        #Test with a string
        self.assertEqual('candyCane', camelCase.camelCase("Candy cane"))
        self.assertEqual ('jack_AndThe7thDoor', camelCase.camelCase("Jack _ and the 7th door"))

    def test_camelCase_with_beginning_number(self):
        with self.assertRaises(CamelError):
            camelCase.camelCase('7 league boots')

    def test_camelCase_with_special_characters(self):
        with self.assertRaises(CamelError):
            camelCase.camelCase("@#$%^!&*()+-=[]{};\':\",./<>?`~")

    def test_camelCase_with_keyword(self):
        with self.assertRaises(CamelError):
            camelCase.camelCase("and")