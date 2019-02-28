#importing unittest module
import unittest
#importing the fustion from the file
from list_sort import sort
#defining the testing class that inherits from the unittest.TestCase
class NumTestCase(unittest.TestCase):
#writing methods to test the cases of the function's behaviour 
     def test_sorted_num(self):
        result = sort([2,3,4,5,6,7,8,9,3.1,4.2,"a","b","c"])
        self.assertEqual(result, {'even': [2, 4, 6, 8], 'odd': [3, 5, 7, 9, 3.1, 4.2], 'chars': ['a', 'b', 'c']}
 )

if __name__ == '__main__':
   unittest.main()
   