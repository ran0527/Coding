class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while n not in d:
            d.add(n)
            temp = n
            sum = 0
            while temp != 0:
                digit = temp % 10
                sum += digit * digit
                temp /= 10
            n = sum
        if n == 1:
            return True
        return False
