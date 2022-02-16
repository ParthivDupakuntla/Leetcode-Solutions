# Max heap, solved the first time, on my own. I am beginning to recognise heap patterns
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maxHeap = []
        wordsDict = defaultdict(int)
        for w in words:
            wordsDict[w]+=1
        
        for w, cnt in wordsDict.items():
            maxHeap.append([-cnt,w])
        
        heapq.heapify(maxHeap)
        
        answer = []
        
        while k>0:
            cnt, w = heapq.heappop(maxHeap)
            answer.append(w)
            k-=1
        return answer
        
