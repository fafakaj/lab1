import unittest

def simplesum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                return[i, j]
    return "NO"

class TestMySum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(simplesum([1,2,3,4,5], 6), [0,4])

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)  # для интерактивных сред
