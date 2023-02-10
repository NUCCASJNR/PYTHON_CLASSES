import unittest
add = __import__("add").add

class integer(unittest.TestCase):
    def test_int(self):
        """Implementing the assertequal method check"""
        self.assertEqual(add(2, 3), 5)
    
    def test_float(self):
        self.assertEqual(add(2.3, 9), 11)
    
    def test_negative_int(self):
        """Implementing the assertNotEqual method check"""
        self.assertNotEqual(add(-9, 9), 8)
    
    def test_is(self):
        """Implementing the assertIs method check"""
        self.assertIs(add(6, 6), 12)
    
    def test_is_not(self):
        """Implementing the assertisNot method check"""
        self.assertIsNot(add(9, 3), 2)

    def test_instance(self):
        """Implementing the assertIsInstance Method check""" 
        self.assertIsInstance(add(3, 5), int)
        
          
          
if __name__ == "__main__":
    unittest.main()