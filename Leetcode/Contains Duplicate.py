class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = set()
        for i in nums:
            if i in memo:
                return True
            memo.add(i)
        return False
