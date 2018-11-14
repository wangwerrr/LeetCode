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
        head = root
        self.helper(root)
        return head
        
    def helper(self, root):
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.right)
        self.invertTree(root.left)
        
