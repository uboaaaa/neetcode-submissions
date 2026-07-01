# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        d = collections.deque([root])
        res = []

        while d:
            d_len = len(d)
            level = []
            for _ in range(d_len):
                node = d.popleft()
                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
                level.append(node.val)
            res.append(level)
        
        return res