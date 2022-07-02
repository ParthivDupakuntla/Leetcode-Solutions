class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxht = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            maxht = max(maxht, horizontalCuts[i] - horizontalCuts[i-1])
        
        maxwdt = max(verticalCuts[0], w-verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            maxwdt = max(maxwdt, verticalCuts[i] - verticalCuts[i-1])
        
        return (maxht * maxwdt) % (10**9 + 7)
