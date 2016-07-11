class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        bin(n), 0b1
        oct(n), 01
        int(n), int(x, n), 1
        hex(n), 0x1
        """
        int_a = int(a, 2)
        int_b = int(b, 2)

        return bin(int_a + int_b)[2:]
