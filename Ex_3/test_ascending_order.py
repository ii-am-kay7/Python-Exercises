import unittest
import ascending_order as a

class MyTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEquals(a.sort([31, 31, 31]), "31 31 31")

    def test_teens(self):
        self.assertEquals(a.sort([17, 11, 19]), "11 17 19")

    def test_negatives(self):
        self.assertEquals(a.sort([-1, -2, -3]), "-3 -2 -1")

    def test_mixed(self):
        self.assertEquals(a.sort([0, 31, -17]), "-17, 0, 31")

if __name__ == "__main__":
    unittest.main()