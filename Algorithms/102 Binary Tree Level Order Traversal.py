# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if root == None:
            return res
        if len(res) < depth+1:
            res.append([])
        res[depth].append(root.val)
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)
#BFS
class Solution(object):
    def levelOrder(self, root):
        if root is None: return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left: record.append(node.left)
                if node.right: record.append(node.right)
            if record: q.append(record)
        return [[x.val for x in level] for level in q]
