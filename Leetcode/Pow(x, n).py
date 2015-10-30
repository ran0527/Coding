# 1 recursion
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1.0/self.myPow(x, -n)

        result = self.myPow(x, n//2)
        if n % 2 ==0:
            return result*result
        else:
            return result*result*x

# 2 iterative
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0/self.myPow(x, -n)

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n /= 2
        return result
