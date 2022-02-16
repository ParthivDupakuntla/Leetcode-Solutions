class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        answer = []
        answer.append(intervals[0])
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            lastEnd = answer[-1][1]
            if start <= lastEnd:
                answer[-1][1] = max(end, lastEnd)
            else:
                answer.append([start,end])
        return answer
        
