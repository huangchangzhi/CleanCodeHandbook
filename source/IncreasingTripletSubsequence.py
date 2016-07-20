# -*- coding:utf8 -*-
class Solution(object):
    """
    Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

    Formally the function should:
    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
    Your algorithm should run in O(n) time complexity and O(1) space complexity.

    Examples:
    Given [1, 2, 3, 4, 5],
    return true.

    Given [5, 4, 3, 2, 1],
    return false.
    """

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

            min1, mid1
            min2

            6,5,4,7,5,2,7
            6,5,4,7,5,2,3,4
        """

        if len(nums) < 3:
            return False

        # len!=0 before call
        min1 = nums[0]
        mid1 = nums[0]
        min2 = nums[0]

        index = 0

        # find first middle
        for index_, num in enumerate(nums[1:]):
            if num < min1:
                min1 = num
            elif num > min1:
                index = index_ + 1
                mid1 = num
                break

        for num in nums[index + 1:]:
            if num > mid1:
                return True

            elif num < mid1:
                if num > min1:
                    mid1 = num
                elif num < min1:
                    if num < min2:
                        min2 = num
                    elif num > min2:
                        mid1 = num
                        min1 = min2

        return False


import unittest


class TestIncreasing(unittest.TestCase):
    s = Solution()

    def test_001(self):
        self.assertTrue(self.s.increasingTriplet([1, 2, 3, 4, 5]))

    def test_002(self):
        self.assertFalse(self.s.increasingTriplet([5, 4, 3, 2, 1]))

    def test_003(self):
        self.assertTrue(self.s.increasingTriplet([6, 5, 4, 7, 5, 2, 7]))

    def test_004(self):
        self.assertTrue(self.s.increasingTriplet([6, 5, 4, 7, 5, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
