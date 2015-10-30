class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        memo = {1:1, 2:2}
        return self.cilmbStairs_helper(n, memo)

    def cilmbStairs_helper(self, n, memo):
        if n not in memo:
            memo[n] = self.cilmbStairs_helper(n - 1, memo) + self.cilmbStairs_helper(n - 2, memo)
        return memo[n]
