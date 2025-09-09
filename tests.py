import unittest
from sumoftwo import simplesum

class TestMySum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(simplesum([1,2,3,4,5], 6), [0,4])
    def test_2(self):
        self.assertEqual(simplesum([2,7,11,15], 9), [0,1])
    def test_3(self):
        self.assertEqual(simplesum([3,2,4], 6), [1,2])
    def test_4(self):
        self.assertEqual(simplesum([3,3], 6), [0,1])
    def test_5(self):
        self.assertEqual(simplesum([3,2,"dsds"], 5), [0,1])
    def test_6(self):
        self.assertEqual(simplesum(["sasasa",4,8,2], 10),[2,3])
    def test_7(self):
        self.assertEqual(simplesum([1,2,3,4], 100),"NO")

if __name__ == '__main__':
    unittest.main()