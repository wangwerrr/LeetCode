# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = [] 
        self.helper(root, sum, [], ans)
        return ans
        
    def helper(self, root, sum, tmp, ans) :   
        if not root:
            return    
        if not root.left and not root.right and root.val == sum:
            ans.append(tmp + [root.val])
            return 
        
        self.helper(root.left, sum-root.val, tmp + [root.val], ans)
        self.helper(root.right, sum-root.val, tmp + [root.val], ans)
