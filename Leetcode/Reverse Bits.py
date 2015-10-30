class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        mask = 1
        for i in range(32):
            if n & mask:
                result += 1
            if i != 31:
                result <<= 1
            mask <<= 1
        return result
        
