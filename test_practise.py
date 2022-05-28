import unittest
from practise import *

class Test(unittest.TestCase):
    def test_values(self):
        self.assertEqual(get_info('#PQU2UJPUJ')['name'], 'bielikovv')
        self.assertEqual(get_info('#PQU2UJPUJ')['expLevel'], 9)
        self.assertEqual(get_info('#PQU2UJPUJ')['arena']['name'], 'Arena 12')

    def test_tag(self):
        self.assertRaises(AssertionError, get_info, '#aefaefa')
        self.assertRaises(AssertionError, get_info, '#aefaefaфуафуа')

    def test_tag_exists(self):
        self.assertRaises(FileExistsError, get_info, '#TEN4NEJ7G')
        self.assertRaises(FileExistsError, get_info, '#PQU2UJPU1')

    def test_is_upper_tag(self):
        self.assertRaises(ValueError, get_info, '#Tgv4CdSt9')
        self.assertRaises(ValueError, get_info, '#cBLECdTt1')

    def test_syntax_tag(self):
        self.assertRaises(SyntaxError, get_info, '#%CH1UTYMA')
        self.assertRaises(SyntaxError, get_info, '#CH1?TY*&M')






