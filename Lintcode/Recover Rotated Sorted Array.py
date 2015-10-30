class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
# 1
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return []

        n = len(nums)
        min_val = min(nums)
        k = 0
        for i in range(len(nums)):
            if nums[i] == min_val:
                k = i

        nums.reverse()
        self.reverse_sublist(nums, 0, n-k-1)
        self.reverse_sublist(nums, n-k, n-1)


    def reverse_sublist(self, lst, start, end):
        while start < end:
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1

# 2
    def recoverRotatedSortedArray(self, nums):
            # write your code here
            if len(nums) == 0:
                return []

            n = len(nums)
            min_val = min(nums)
            k = 0
            for i in range(len(nums)):
                if nums[i] == min_val:
                    k = i

            nums.reverse()
            nums[0:n-k] = reversed(nums[0: n-k])
            nums[n-k:n] = reversed(nums[n-k:n])
