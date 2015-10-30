class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        for number in nums:
            if number not in memo:
                memo[number] = 1
            else:
                memo[number] += 1
        for pair in memo:
            if memo[pair] == 1:
                return pair
