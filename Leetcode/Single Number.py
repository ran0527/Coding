class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = nums[0]
        for i in range(1, len(nums)):
            p = p ^ nums[i]
        return p

        
