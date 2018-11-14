# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        ans = []
        self.helper(root, "", ans)
        return ans
        
    def helper(self, root, tmp, ans) :   
        if not root.left and not root.right: # leaf node judgement
            ans.append(tmp + str(root.val))
            return    
        if root.left:
            self.helper(root.left, tmp + str(root.val) + "->", ans )
        if root.right:
            self.helper(root.right, tmp  + str(root.val) + "->", ans)
