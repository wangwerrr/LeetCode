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
        return self.isMirror(root, root)
    def isMirror(self, r1, r2):
        if r1 is None or r2 is None:
            return r1 == r2
        
        return r1.val == r2.val and self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)

    # helper func: isMirror to check if the tree and its reflection are the same
