# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #perform dfs to check vaLue of the current node wrt its local root
        # if node value >= root value, increase counter
        #write a dfs func that returns true, and count the number of times it returns true or pass a counter (wrong)
        #keep a nonlocal variable to keep count 
        if not root:
            return 0
        def checker(node, currmax):
            nonlocal count
            if not node:
                return 
            if node.val >= currmax:
                count+=1
                currmax = node.val
            checker(node.left, currmax)
            checker(node.right, currmax)
        
        count = 0
        checker(root, -10**4)
        return count
    
