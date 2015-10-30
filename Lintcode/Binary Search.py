# 1
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        first = 0
        last = len(nums)
        while first < last:
            midpoint = (first + last) / 2
            if nums[midpoint] == target:
                while midpoint >= 0 and nums[midpoint - 1] == nums[midpoint]:
                    midpoint -= 1
                return midpoint
            elif target > nums[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint
        return -1

# 2
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        first = 0
        last = len(nums) - 1
        while first < last :
            midpoint = (first + last) / 2
            if nums[midpoint] == target:
                last = midpoint
                continue
            elif target > nums[midpoint]:
                first = midpoint + 1
            elif target < nums[midpoint]:
                last = midpoint

        if nums[first] == target:
            return first
        if nums[last] == target:
            return last
        return -1
        
# 3
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        first = 0
        last = len(nums) - 1
        while first < last :
            midpoint = (first + last) / 2
            if target > nums[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint

        if nums[last] == target:
            return last
        return -1
