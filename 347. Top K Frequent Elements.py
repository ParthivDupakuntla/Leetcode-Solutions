#Top K Implementation with max heap. I solved it in the first attempt. Similar to reorganise string.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        for i in nums:
            countDict[i]+=1
        maxHeap = []
        for num, cnt in countDict.items():
            maxHeap.append([-cnt,num])
        heapq.heapify(maxHeap)
        
        answer = []
        while k:
            cnt, num = heapq.heappop(maxHeap)
            answer.append(num)
            k-=1
        return answer
            
