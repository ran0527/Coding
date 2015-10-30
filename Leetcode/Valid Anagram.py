# 1 sort
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# 2 hash table
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for j in t:
            if j not in dict:
                return False
            else:
                dict[j] -= 1
            if dict[j] < 0:
                return False

        return True
