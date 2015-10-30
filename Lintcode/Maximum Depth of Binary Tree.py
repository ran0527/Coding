"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        # leaf node
        if root == None:
            return 0

        left_child_depth = self.maxDepth(root.left)
        right_child_depth = self.maxDepth(root.right)
        return max(left_child_depth, right_child_depth) + 1
