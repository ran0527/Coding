class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        memo = {1:0, 2:1}
        return self.helper(n, memo)

    def helper(self, n, memo):
        if not n in memo:
            memo[n] = self.helper(n-1, memo)+self.helper(n-2, memo)
        return memo[n]
