#1
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
                num = num / 2
            else:
                num = num / 2
        return count

#2
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
                num = num >> 1
            else:
                num = num >> 1
        return count
