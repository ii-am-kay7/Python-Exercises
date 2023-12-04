import unittest
import fizzbuzz as f

class MyTestCase(unittest.TestCase):
    def test_0(self):
        self.assertEquals(f.fizzbuzz(0), [])

    def test_3(self):
        self.assertEquals(f.fizzbuzz(3), ["1","2","fizz"])

    def test_5(self):
        self.assertEquals(f.fizzbuzz(5), ["1","2","fizz","4","buzz"])

    def test_20(self):
        self.assertEquals(f.fizzbuzz(5), ["1","2","fizz","4","buzz","fizz","7",
        "8","fizz","buzz","11","fizz","13","14","fizzbuzz","16","17","fizz","19","buzz"])

if __name__ == "__main__":
    unittest.main()