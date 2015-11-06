class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        result = 0
        while n >= i:
            result += n / i
            i *= 5
        return result

        
