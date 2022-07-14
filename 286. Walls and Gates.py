'''
Working backwards, start from gates and check the distance. It is always going to be the shortest distance because of level tranversal of bfs
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        rows = len(rooms)
        cols = len(rooms[0])
        empty = 2**31 - 1
        if rows == 0:
            return
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            r,c = q.popleft()
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr,dc in dirs:
                row = r + dr
                col = c + dc
                if row < 0 or col < 0 or row >= rows or col >= cols or rooms[row][col] != empty:
                    continue
                rooms[row][col] = rooms[r][c]+1
                q.append((row,col))
        
