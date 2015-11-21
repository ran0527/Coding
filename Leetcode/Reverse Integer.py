class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        while x > 0:
            ans = ans * 10 + x % 10
            x /= 10
        if ans > 2147483647:
            return 0
        return sign * ans
