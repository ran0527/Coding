class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        j = 1
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
              A[j] = A[i]
              j += 1
        return j
