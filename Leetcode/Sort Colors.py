# 1
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1
            elif nums[i] == 2:
                count_2 += 1
            else:
                return []

        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_0 + count_1):
            nums[i] = 1
        for i in range(count_0 + count_1, len(nums)):
            nums[i] = 2

# 2
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1
            elif nums[i] == 2:
                count_2 += 1
            else:
                return []

        count_dict = {0:count_0, 1:count_1,2:count_2}

        # the tail of sorted part
        k = 0
        # iterate over dict
        for count_key in count_dict:
            # for i in [0, count_vale)
            for i in range(count_dict[count_key]):
             # update value to be the key
                nums[k] =  count_key
                # tail moves right
                k += 1
# 3
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1
            elif nums[i] == 2:
                count_2 += 1
            else:
                return []

        count_dict = {0:count_0, 1:count_1,2:count_2}

        # the tail of sorted part
        k = 0
        # iterate over dict
        for count_key in sorted(count_dict.keys()):
            # for i in [0, count_vale)
            for i in range(count_dict[count_key]):
             # update value to be the key
                nums[k] =  count_key
                # tail moves right
                k += 1
# 4
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # init to empty dictionary
        count_dict = {}
        # iterate nums
        for m in nums:
            if m in count_dict:
                count_dict[m] += 1
            else:
                count_dict[m] = 1

        # the tail of sorted part
        k = 0
        # iterate over dict
        for count_key in sorted(count_dict.keys()):
            # for i in [0, count_vale)
            for i in range(count_dict[count_key]):
             # update value to be the key
                nums[k] =  count_key
                # tail moves right
                k += 1
            
