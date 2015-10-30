"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        #subtree T1 equals subtree T2
        if self.identical_tree(T1, T2):
            return True
        if T1 == None:
            return False
        elif self.isSubtree(T1.left, T2):
            return True
        elif self.isSubtree(T1.right, T2):
            return True
        else:
            return False

    def identical_tree(self, T1, T2):
        if T1 == None and T2 == None:
            return True
        elif T1 == None and T2 != None:
            return False
        elif T1 != None and T2 == None:
            return False

        b1 = T1.val == T2.val
        b2 = self.identical_tree(T1.left, T2.left)
        b3 = self.identical_tree(T1.right, T2.right)
        return b1 and b2 and b3
            
