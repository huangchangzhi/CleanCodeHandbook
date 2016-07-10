# -*- coding: utf8 -*-

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # if n == 0:
        #     return 0
        #
        # if n == 1:
        #     return 1
        #
        # if n == 2:
        #     return 2

        if n <= 0:
            return 0

        if n == 1 or n == 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n):
        """
        """
        if n <= 0:
            return 0

        if n == 1 or n == 2:
            return n

        v_pre = 1
        v_curr = 2
        index = 2
        v_next = 0
        while index < n:
            v_next = v_pre + v_curr
            index += 1

            v_pre, v_curr = v_curr, v_next

        return v_next

    def climbStairs3(self, n):
        """
        """
        if n <= 0:
            return 0

        if n == 1 or n == 2:
            return n

        v_pre = 1
        v_curr = 2
        index = 2
        v_next = 3
        while index < n:
            v_next, v_pre, v_curr = v_curr + v_pre, v_curr, v_next
            index += 1

        return v_next


s = Solution()
print s.climbStairs2(3)
print s.climbStairs2(4)
