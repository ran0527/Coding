class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ans = strs[0]
        for string in strs[1:]:
            n = len(string)
            for i, c in enumerate(ans):
                if i >= n or ans[i] != string[i]:
                    ans = ans[:i]
                    break
        return ans
        
