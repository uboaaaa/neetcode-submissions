# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minval, maxval = float('-inf'), float('inf')

        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right): return False

            return dfs(node.left, left, min(node.val, right)) and dfs(node.right, max(node.val, left), right)
        
        return dfs(root, minval, maxval)
                 
            
