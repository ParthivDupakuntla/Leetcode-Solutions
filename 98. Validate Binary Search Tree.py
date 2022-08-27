# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checker(node, u, l):
            if not node:
                return True
            if not (node.val<u and node.val > l):
                return False
            return checker(node.left, node.val,l) and checker(node.right,u,node.val)
        return checker(root, float("inf"), float("-inf"))

        
