import unittest
import leap_year as l

class MyTestCase(unittest.TestCase):
    def test_2012(self):
        self.assertEquals(l.leap_year(2012), True)

    def test_2016(self):
        self.assertEquals(l.leap_year(2016), True)

    def test_4(self):
        self.assertEquals(l.leap_year(4), True)

    def test_2010(self):
        self.assertEquals(l.leap_year(2010), False)

    def test_2018(self):
        self.assertEquals(l.leap_year(2018), False)

    def test_2021(self):
        self.assertEquals(l.leap_year(2021), False)

if __name__ == "__main__":
    unittest.main()