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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root == None:
            return []

        left_child_preorder = self.preorderTraversal(root.left)
        right_child_preorder = self.preorderTraversal(root.right)
        return [root.val] + left_child_preorder + right_child_preorder
