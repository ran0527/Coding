class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        result = []
        numbers.sort()
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[i] + numbers[right]
                if result == [] or abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return result
