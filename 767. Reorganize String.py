https://leetcode.com/problems/reorganize-string/

#Max heap implementation
# take the most frequent, add it to the result
# hold it if its count is not zero, that means it is still there.
# next iteration, pop the next frequent one. 
# now add the previous one to the max heap and set the previous to None again
# if there is a previous one, and the maxheap is empty, that means there is a character that was just added, so return empty string.

class Solution:
    def reorganizeString(self, s: str) -> str:
        countDict = defaultdict(int)
        for char in s:
            countDict[char]+=1
        maxHeap = []
        for char,cnt in countDict.items():
            maxHeap.append([-cnt,char])
        heapq.heapify(maxHeap)
        
        prev = None
        answer = ""
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
                
            cnt, char = heapq.heappop(maxHeap)
            answer+= char
            cnt +=1
            
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt!=0:
                prev = [cnt, char]
        return answer
