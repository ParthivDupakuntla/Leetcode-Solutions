#Min heap solution. Consider the matrix as n sorted lists. Store (element, currentRow, currentCol) tuple in min heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minH = []
        for i in range(len(matrix)):
            minH.append((matrix[i][0], i, 0))
        heapq.heapify(minH)
        
        while k:
            curr, r, c = heapq.heappop(minH)
            if c < len(matrix)-1:
                heapq.heappush(minH, (matrix[r][c+1], r, c+1))
            k-=1
        return curr
                               
