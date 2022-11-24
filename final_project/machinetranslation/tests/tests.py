import sys
sys.path.append("..") # Adds higher directory to python modules path.
import unittest
from translator import english_to_french,french_to_english

class Test(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(french_to_english(""), "")
    
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
