class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        g = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    g[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        g[i][j] = 1
                    elif i == 0:
                        g[i][j] = g[i][j-1]
                    elif j == 0:
                        g[i][j] = g[i-1][j]
                    else:
                        g[i][j] = g[i][j-1] + g[i-1][j]
        return g[m-1][n-1]
