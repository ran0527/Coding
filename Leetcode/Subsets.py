# 1 Bit Manipulation
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort(reverse = True)
        n = len(nums)
        result = []
        for i in range(pow(2, n)):
            mask = 1
            path = []
            for j in range(n):
                if mask & i != 0:
                    path.append(nums[-(j+1)])
                mask <<= 1
            result.append(path)
        return result

# 2 Recursion
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        path = []
        self.recursive(nums, result, path)
        return result

    def recursive(self, nums, result, path):
        result.append(list(path))
        for i in range(len(nums)):
            path.append(nums[i])
            self.recursive(nums[i+1:], result, path)
            path.pop()
