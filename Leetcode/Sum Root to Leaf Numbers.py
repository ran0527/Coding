# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, sum):
        if root == None:
            return 0
        sum = sum * 10 + root.val
        if root.left == None and root.right == None:
            return sum
        left = self.helper(root.left, sum)
        right = self.helper(root.right, sum)
        return left + right



        
