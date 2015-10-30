# 1
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        opt = [0] * (n+1)
        if n == 0:
            return opt[0]
        opt[1] = A[0]
        if n <= 1:
            return opt[n]

        opt[2] = max(A[0], A[1])
        for i in range(3, len(A) + 1):
            opt[i] = max(opt[i-2]+A[i-1], opt[i-1])
        return opt[n]

# 2
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        opt = [0] * (n+1)
        if n == 0:
            return opt[0]
        opt[1] = A[0]
        if n <= 1:
            return opt[n]
        for i in range(2, len(A) + 1):
            opt[i] = max(opt[i-2]+A[i-1], opt[i-1])
        return opt[n]
# 3
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        opt = [0] * (n+1)
        if n == 0:
            return opt[0]
        opt[1] = A[0]
        for i in range(2, len(A) + 1):
            opt[i] = max(opt[i-2]+A[i-1], opt[i-1])
        return opt[n]


        
