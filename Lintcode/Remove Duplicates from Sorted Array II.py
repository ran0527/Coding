class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        j = 0
        for i in range(len(A)):
            if j < 2 or A[j - 2] != A[i]:
                A[j] = A[i]
                j += 1
        return j
