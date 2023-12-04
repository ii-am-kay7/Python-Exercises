import unittest
import reverser as r

class MyTestCase(unittest.TestCase):
    def test_19(self):
        self.assertEquals(r.reverse(19), 91)

    def test_123(self):
        self.assertEquals(r.reverse(123), 321)

    def test_1024(self):
        self.assertEquals(r.reverse(1024), 4201)

    def test_11034(self):
        self.assertEquals(r.reverse(11034), 43011)

    def test_1(self):
        self.assertEquals(r.reverse(1), 1)

if __name__ == "__main__":
    unittest.main()