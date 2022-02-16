# 2 Heaps detailed explanation
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        # if small heap's largest number is greater than large heap's smallest, we need to remove that from small heap and insert in large heap
        
        if self.small and self.large and ((-1*self.small[0])>self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        
        #if small heap has more elements:
        if len(self.small)>len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        #if large heap has more elements:
        if len(self.large)>len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        
        
        
        

    def findMedian(self) -> float:
        #if small heap is bigger, the max of small heap is the median
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        #if large heap is bigger, the min of large heap is the median
        if len(self.large)>len(self.small):
            return self.large[0]
        #if both of them are equal size, then median is the average of the max of small heap and min of large heap
        maxSmall = -1*self.small[0]
        minLarge = self.large[0]
        return (maxSmall+minLarge)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
