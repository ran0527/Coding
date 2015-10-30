# 1
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num /= 10
            num = temp
        return num

# 2
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
