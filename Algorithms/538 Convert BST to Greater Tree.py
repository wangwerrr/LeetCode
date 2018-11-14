# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.dfs(root)
        return root

    def dfs(self, cur):
        if cur == None:
            return       
        self.dfs(cur.right)
        self.sum  = self.sum + cur.val
        cur.val = self.sum
        self.dfs(cur.left)
            
# reversed Inorder Traversal (LDR) 
        
        
