class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))

    def rob_linear(self, nums):
        n = len(nums)
        opt = [0] * (n+1)
        if n == 0:
            return opt[0]
        opt[1] = nums[0]
        for i in range(2, len(nums) + 1):
            opt[i] = max(opt[i-2]+nums[i-1], opt[i-1])
        return opt[n]

        
