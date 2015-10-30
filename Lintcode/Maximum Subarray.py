class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
# O(n) time, O(n) space
    '''def maxSubArray(self, nums):
        # write your code here
        opt = [0] * (len(nums) + 1)
        for x in range(1, len(nums) + 1):
            opt[x] = max(nums[x-1], opt[x-1] + nums[x-1])
        result = -sys.maxint
        for i in range(len(nums)):
            result = max(result, opt[i+1])
        return result'''

# O(n) time, O(1) space
    def maxSubArray(self, nums):
        # write your code here
        opt = 0
        result = -sys.maxint

        for x in range(1, len(nums) + 1):
            opt = max(nums[x-1], opt + nums[x-1])
            result = max(result, opt)
        return result

    '''def maxSubArray(self, nums):
        # write your code here
        max_val = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            max_val = max(max_val, sum)
        return max_val'''
