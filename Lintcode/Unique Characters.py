class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        visited = []
        for i in str:
            if i in visited:
                return False
            visited.append(i)
        return True
