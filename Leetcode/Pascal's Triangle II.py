# 1
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        list = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                list[i][j] = list[i-1][j-1] + list[i-1][j]
        return list[rowIndex]

# 2
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        list_current = [1]
        for i in range(rowIndex):
            list_previous = list_current
            list_current = [1]
            for j in range (1, len(list_previous)):
                list_current.append(list_previous[j-1] + list_previous[j])
            list_current.append(1)
        return list_current
