class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        memo = {}
        for i in range(len(numbers)):
            if not (target-numbers[i]) in memo:
                memo[numbers[i]] = i
            else:
                index1 = memo[target-numbers[i]]
                index2 = i
        return [index1 + 1, index2 + 1]
