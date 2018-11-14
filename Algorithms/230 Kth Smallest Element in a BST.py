# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root, ls):
        if root == None:
            return
        
        self.helper(root.left, ls)
        ls.append(root.val)
        self.helper(root.right, ls) 

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        output = []
        self.helper(root, output)
        return output[k-1]
        
        
        
