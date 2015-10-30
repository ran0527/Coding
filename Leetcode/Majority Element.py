# 1 O(n) Time,  O(n) Space
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        memo = {}
        for element in nums:
            if element not in memo:
                memo[element] = 1
            else:
                memo[element] += 1
        for element in memo:
            if memo[element] > n:
                return element

# 2 O(n) Time, O(1) Space
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major_element = nums[0]
        major_times = 1

        for element in nums[1:]:
            if element == major_element:
                major_times += 1
            elif major_times == 0:
                major_times = 1
                major_element = element
            else:
                major_times -= 1
        return major_element

        
