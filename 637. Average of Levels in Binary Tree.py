# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        ans = []
        if not root:
            return [0]
        q.append(root)
        while q:
            su = 0
            currlen = len(q)
            for i in range(currlen):
                node = q.popleft()
                su += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(su/currlen)
        return ans
                
