#importing unittest module
import unittest
#importing the fustion from the file
from extra import find
#defining the testing class that inherits from the unittest.TestCase
class MissTestCase(unittest.TestCase):
#writing methods to test the cases of the function's behaviour 
     def test_Miss(self):
        result = find([1,3,5,7,9])
        self.assertEqual(result, [0, 2, 4, 6, 8])
 