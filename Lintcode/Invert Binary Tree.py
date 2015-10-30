"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        self.helper(root)
        return

    def helper(self, root):
        if root == None:
            return None
        new_left_child = self.helper(root.right)
        new_right_child = self.helper(root.left)
        root.left = new_left_child
        root.right = new_right_child
        return root
