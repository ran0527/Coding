class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while num % factor == 0:
                num /= factor
        if num == 1:
            return True
        return False

        
