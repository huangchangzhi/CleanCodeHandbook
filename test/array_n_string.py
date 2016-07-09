# -*- coding: utf8 -*-

import unittest

from source.array_n_string import *


class TestTwoSum(unittest.TestCase):
    def test_two_sum_001(self):
        numbers = [1, 2, 3, 4, 5]
        target = 8
        index1, index2 = TwoSum().two_sum(numbers, target)

        self.assertEqual(index1, 3, 'first value error:[%d]' % index1)
        self.assertEqual(index2, 5, 'first value error:[%d]' % index2)

    def test_two_sum_002(self):
        numbers = [1, 2, 3, 4]
        target = 8

        try:
            TwoSum().two_sum(numbers, target)
        except ValueError:
            pass


class TestSortedTwoSum(unittest.TestCase):
    def test_sorted_two_sum_001(self):
        numbers = [1, 2, 3, 4, 5]
        target = 8
        index1, index2 = SortedTwoSum().two_sum(numbers, target)

        self.assertEqual(index1, 3, 'first value error:[%d]' % index1)
        self.assertEqual(index2, 5, 'first value error:[%d]' % index2)

    def test_sorted_two_sum_002(self):
        numbers = [1, 2, 3, 4]
        target = 8

        try:
            TwoSum().two_sum(numbers, target)
        except ValueError:
            pass


class TestTwoSumClass(unittest.TestCase):
    def test_two_sum_class_001(self):
        t = TwoSumClass()
        t.add(1)
        t.add(3)
        t.add(2)
        self.assertEqual(True, t.find(4), '1+3=4')
        self.assertEqual(False, t.find(7), 'no find 7')

        t.add(4)
        self.assertEqual(True, t.find(7), '4+3=7')
        self.assertEqual(False, t.find(8), 'no find 8')

        t.add(4)
        self.assertEqual(True, t.find(8), '4+4=8')


class TestValidPalindrome(unittest.TestCase):
    #     def terst_
    pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testTwoSum']
    unittest.main()
