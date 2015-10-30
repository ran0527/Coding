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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if root == None:
            return []

        left_child_postorder = self.postorderTraversal(root.left)
        right_child_postorder = self.postorderTraversal(root.right)
        return left_child_postorder + right_child_postorder + [root.val]
