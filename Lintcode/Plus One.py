class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        i = len(digits) - 1
        if digits[i] < 9:
            digits[i] += 1
        else:
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i == -1:
                digits.insert(0, 1)
            else:
                digits[i] += 1
        return digits
