# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxval):
            nonlocal res
            if not node:
                return

            if maxval <= node.val:
                res += 1
            maxval = max(maxval, node.val)
            
            dfs(node.left, maxval)
            dfs(node.right, maxval)
        
        dfs(root, float('-inf'))
        return res
