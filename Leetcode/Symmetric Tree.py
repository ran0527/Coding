# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left != None and root.right != None:
            return self.helper(root.left, root.right)
        return False

    def helper(self, left, right):
        if left == None and right == None:
            return True
        if left != None and right != None:
            return (left.val == right.val) and self.helper(left.left, right.right) and self.helper(left.right, right.left)
        return False
        
