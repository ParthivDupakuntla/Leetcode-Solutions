class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def area(r,c):
            if r < 0 or r >=rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c]==0:
                return 0
            visited.add((r,c))
            return(area(r+1,c) + area(r-1,c) + area(r,c+1) + area(r,c-1) +1)
        ans = float("-inf")
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, area(i,j))
        return ans
                
            
