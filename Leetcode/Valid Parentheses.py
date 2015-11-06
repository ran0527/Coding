class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '[':']', '{':'}' }
        stack = []

        for character in s:
            if character == '(' or character == '[' or character == '{':
                stack.append(character)
            elif len(stack) == 0 or dict[stack[-1]] != character:
                return False
            else:
                stack.pop()
        return len(stack) == 0
            
