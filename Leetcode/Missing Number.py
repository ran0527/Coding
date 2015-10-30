class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = n * (n + 1) / 2
        result = 0
        for i in nums:
            result += i
        return sum - result
