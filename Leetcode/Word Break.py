class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        state = []
        cache = {}
        return self.recursive(s, wordDict, state, cache)

    def recursive(self, s, wordDict, state, cache):
        if s in cache:
            return cache[s]

        print "recursive: ", state, s
        if len(s) == 0:
            cache[s] = True
            return True

        matches = self.getMatches(s, wordDict)
        print "matches: ", matches

        for match in matches:
            state.append(match)
            if self.recursive(s[len(match):], wordDict, state, cache):
                cache[s] = True
                return True
            state.pop()
        cache[s] = False
        return False

    def getMatches(self, s, wordDict):
        result = []
        for i in range(1, len(s)+1):
            substr = s[:i]
            if substr in wordDict:
                result.append(substr)
        return result


        
