# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        new_left_child = self.invertTree(root.left)
        new_right_child = self.invertTree(root.right)
        root.left = new_right_child
        root.right = new_left_child
        return root
        
