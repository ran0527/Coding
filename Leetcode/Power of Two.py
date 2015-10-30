# 1 # 1 bit = 1
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        while n > 0:
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result == 1

# 2
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n-1) == 0
