class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        lst = []
        for i in range(n):
            if nums[i] not in lst:
                lst.append(nums[i])
            else:
                lst.remove(nums[i])
        return lst

        
