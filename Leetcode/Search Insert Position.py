class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        positon = 0

        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                position = mid
            else:
                left = mid + 1
                position = mid + 1
        return position
                
