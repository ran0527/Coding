class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
#6 O(n) time, O(1) space
    def minSubArray(self, nums):
        # write your code here
        opt = 0
        result = sys.maxint

        for x in range(1, len(nums) + 1):
            opt = min(opt + nums[x-1], nums[x-1])
            result = min(result, opt)

        return result


#5 O(n) time, O(n) space
    '''def minSubArray(self, nums):
        # write your code here
        opt = [0] * (len(nums) + 1)

        for x in range(1, len(nums) + 1):
            opt[x] = min(opt[x-1] + nums[x-1], nums[x-1])

        result = sys.maxint
        for i in range(len(nums)):
            result = min(result, opt[i+1])

        return result'''


#4  O(n^2) time, O(1) space
    '''def minSubArray(self, nums):
        # write your code here
        min_sum = sys.maxint
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    sum = nums[i]
                else:
                    sum += nums[j]
                min_sum = min(min_sum, sum)
        return min_sum'''

#3  O(n^3) time, O(1) space
    '''def minSubArray(self, nums):
        # write your code here
        min_sum = sys.maxint
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j + 1):
                # sum of sub array from i to j
                    sum += nums[k]
                min_sum = min(min_sum, sum)
        return min_sum'''

#2  O(n^3) time, O(1) space
    '''def minSubArray(self, nums):
        # write your code here
        min_sum = sys.maxint
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # sum of sub array from i to j
                sum = self.getSum(nums, i, j)
                min_sum = min(min_sum, sum)
                # print i, j, sum, min_sum
                # print j
                # print sum
                # print min_sum
        return min_sum

    def getSum(self, arr, i ,j):
        sum = 0
        for k in range(i, j + 1):
            sum += arr[k]
        return sum'''


#1  Wrong
    '''sum = 0
        min_sum = nums[0]
        for i in range(len(nums)):
            if nums[i] < 0:
                sum += nums[i]
            else:
                min_sum = min(min_sum, nums[i])
        if min_sum > 0 and sum == 0:
            return min_sum
    return sum'''
