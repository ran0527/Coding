class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list = [[1]*(i+1) for i in range(numRows)]
        if numRows <= 2:
            return list
        for i in range(2, numRows):
            for j in range(1, i):
                list[i][j] = list[i-1][j-1] + list[i-1][j]
        return list

        
