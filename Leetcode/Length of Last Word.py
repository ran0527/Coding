class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = n - 1
        result = 0

        while i >= 0:
            if s[i] != ' ':
                result += 1
            else:
                if result != 0:
                    break
            i -= 1
        return result

            
