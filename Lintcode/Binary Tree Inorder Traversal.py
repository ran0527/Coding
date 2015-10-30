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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if root == None:
            return []

        left_child_inorder = self.inorderTraversal(root.left)
        right_child_inorder = self.inorderTraversal(root.right)
        return left_child_inorder + [root.val] + right_child_inorder
