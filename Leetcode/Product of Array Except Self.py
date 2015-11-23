#1 Time O(n^2)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                arr[i] *= nums[j]
        return arr

#2 Time O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [1] * n
        left = [1, nums[0]]
        right = [1, nums[-1]]
        for i in range(1, n):
            left.append(left[-1] * nums[i])
        for i in range(n-2, -1, -1):
            right.append(right[-1] * nums[i])
        right.reverse()
        for i in range(n):
            arr[i] = left[i] * right[i+1]
        return arr
        
