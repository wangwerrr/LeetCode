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
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.helper(root, output)
        return output

# continue recursion until the condition of base case is met
# get farmiliar with function features in Python (self.func, local variables, etc.)
# solution using stack?
