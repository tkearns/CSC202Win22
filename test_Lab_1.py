import unittest
import Lab1

class TestLab1(unittest.TestCase):
    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( Lab1.bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertRaises(ValueError, Lab1.bin_search, 4, 0, len(list_val), list_val)
        with self.assertRaises(ValueError):
            Lab1.bin_search(4, 0, len(list_val), list_val)

if __name__ == "__main__":
    unittest.main()
