# -*- coding: utf8 -*-


class TwoSum(object):
    """
        Given an array of integers, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices(索引) of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.

    """

    def two_sum(self, numbers, target):

        # 异常场景的提示 1. 输入非法类型；2. 无结果；3. 多个结果；
        # 内容确定：1. 是否有序；2. 是否有重复；
        # # 无序，有且仅有单个结果
        if type(numbers) is not list:
            raise ValueError('wrong input of numbers')
        if type(target) is not int:
            raise ValueError('wrong input of target')

        return self.two_sum_n(numbers, target)

    def two_sum_n2(self, numbers, target):
        index1 = 0
        index2 = 0
        length = len(numbers)
        while index1 < length - 1:
            index2 = index1 + 1
            while index2 < length:
                if numbers[index1] == target - numbers[index2]:
                    return index1 + 1, index2 + 1
                index2 = index2 + 1

            index1 = index1 + 1
        else:
            raise ValueError('no two sum solution')

    def two_sum_n(self, numbers, target):
        numberDict = dict()
        for ind in xrange(len(numbers)):
            if target - numbers[ind] in numberDict:
                return numberDict[target - numbers[ind]] + 1, ind + 1
            else:
                numberDict[numbers[ind]] = ind
        else:
            raise ValueError('no two sum solution')


class SortedTwoSum(object):
    def two_sum(self, numbers, target):
        length = len(numbers)
        begin = 0
        end = length - 1

        while begin < end:
            if numbers[begin] + numbers[end] == target:
                return begin + 1, end + 1
            elif numbers[begin] + numbers[end] < target:
                begin = begin + 1
            else:
                end = end - 1
        raise ValueError("No two sum solution")


class TwoSumClass(object):
    def __init__(self):
        self.dict = dict()

    def add(self, val):
        if val in self.dict:
            self.dict[val] = 2
        else:
            self.dict[val] = 1

    def find(self, target):
        for val in self.dict:
            if target - val in self.dict:
                if val != target - val:
                    return True
                elif self.dict[val] == 2:
                    return True
        else:
            return False


class ValidPalindrome(object):
    def is_palindrome(self, s):
        begin = 0
        end = len(s) - 1
        while begin < end:
            while begin < end and not s[begin].isalpha():
                begin = begin + 1
            while begin < end and not s[end].isalpha():
                end = end - 1

            if s[begin].upper() != s[end].upper():
                return False

            begin = begin + 1
            end = end - 1
        else:
            return True
