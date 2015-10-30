class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        result = []
        n = len(numbers)
        if n < 3:
            return []
        numbers.sort()
        for i in range(n):
            if (i > 0) and (numbers[i] == numbers[i-1]):
                # print "i", i
                continue
            left = i + 1
            right = n - 1
            while left < right:
                three_sum = numbers[left] + numbers[i] + numbers[right]
                if three_sum == 0:
                    # print "Result:", i, left, right
                    if not result or (result[-1] != [numbers[i], numbers[left], numbers[right]]):
                        result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    # print "<", i, left, right
                    left += 1
                else:
                    # print ">", i, left, right
                    right -= 1
        return result
