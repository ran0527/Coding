class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        self.recursive(nums, result, path)
        return result


    def recursive(self, nums, result, path):
        if len(nums) == 0:
            result.append(list(path))
        for i in range(len(nums)):
            path.append(nums[i])
            rest = nums[:i] + nums[i+1:]
            self.recursive(rest, result, path)
            path.pop()
