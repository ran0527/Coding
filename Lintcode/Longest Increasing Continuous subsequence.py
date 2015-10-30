class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        decrease_opt = 1
        increase_opt = 1
        opt1 = 0
        opt2 = 0

        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                decrease_opt = decrease_opt + 1
                opt1 = max(decrease_opt, opt1)
            else:
                decrease_opt = 1

        for j in range(1, len(A)):
            if A[j] > A[j-1]:
                increase_opt = increase_opt + 1
                opt2 = max(increase_opt, opt2)
            else:
                 increase_opt = 1

        result = max(opt1, opt2)
        return result
