class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    q.append((i,j,0))
                    
                    
        visited = set()#can do without it
        while q:
            r,c,val = q.popleft()
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in dirs:
                row = r+dr
                col = c+dc
                if 0<= row < rows and 0 <= col < cols and grid[row][col] in ('#', 'O') and (row,col) not in visited:
                    if grid[row][col] == '#':
                        return val + 1
                    visited.add((row,col))
                    #instead of visited set, can do grid[row][col] = 'any flag' to mark the element visited
                    q.append((row,col,val+1)) #add next element to queue
        return -1                
