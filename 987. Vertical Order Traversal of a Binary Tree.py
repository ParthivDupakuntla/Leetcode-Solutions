# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return
        level_items = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        
        mincol, maxcol = float(inf), float(-inf)
        while queue:
            node, row, col = queue.popleft()
            if col < mincol : 
                mincol = col
            if col > maxcol :
                maxcol = col
            level_items[col].append((node.val, row))
            
            if node.left:
                queue.append([node.left, row+1, col-1])
            if node.right:
                queue.append([node.right, row+1, col+1])
            
        res = []
        for level in range(mincol, maxcol+1):
            items = level_items[level]
            items.sort(key = lambda x : (x[1], x[0]))
            vals = [val for val, row in items]
            res.append(vals)
        return res

    
    
    
"""
Complexity : O(N) + O(NlogN/k), k is the width of the tree essentially NlogN
Solution key points: BFS, create a dict of lists, have 2 pointers for columns, iterate through each column and sort each level based on the row number first and then the value 
Link : https://www.youtube.com/watch?v=_8yW-dQVJHM&ab_channel=CrackingFAANG
"""
        
