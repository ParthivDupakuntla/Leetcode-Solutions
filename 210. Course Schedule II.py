#Kahn's Algorithm for Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        in_degree = [0]*numCourses
        for i in range(numCourses):
            for j in preMap[i]:
                in_degree[j]+=1
        
        q = collections.deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)
            
        
        idx = 0
        result = [0]*numCourses
        while q:
            curr = q.popleft()
            result[idx] = curr
            for i in preMap[curr]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    q.append(i)
            idx+=1
        if idx!=numCourses:
            return []
        else:
            return reversed(result)
                
            
            
        
