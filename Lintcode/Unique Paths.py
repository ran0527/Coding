class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # write your code here
# 1
        if m == 0 or n == 0:
            return 0
        g = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 or j == 0:
                    g[i][j] = 1
                else:
                    g[i][j] = g[i][j-1]+ g[i-1][j]
        return g[m-1][n-1]

# 2
        if m == 0 or n == 0:
            return 0
        g = [[0] * n] * m
        for i in range(m):
            g[i][0] = 1
        for j in range(n):
            g[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] = g[i-1][j] + g[i][j-1]
        return g[m-1][n-1]
