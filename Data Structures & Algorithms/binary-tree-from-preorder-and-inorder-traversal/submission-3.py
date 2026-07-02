# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder: 
            root_val = preorder[0]
        else:
            return
        root = TreeNode(root_val)

        mid = inorder.index(root_val)
        left_nodes, right_nodes = inorder[:mid], inorder[mid+1:]

        root.left = self.buildTree(preorder[1:mid + 1], left_nodes)
        root.right = self.buildTree(preorder[mid + 1:], right_nodes)

        return root