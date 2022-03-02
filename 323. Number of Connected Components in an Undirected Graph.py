#Union Find using Rank
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(n1):
            result = n1
            
            while result!=parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            
            return result
        
        def union(n1,n2):
            parent1, parent2 = find(n1), find(n2)
            
            if parent1 == parent2:
                return 0
            
            if rank[parent1]>rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            
            return 1
        
        result = n
        
        for n1,n2 in edges:
            result -= union(n1,n2)
        
        return result

    
 ------------------------------------------------------------
#DFS Solution

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adjList = defaultdict(list)
        
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        print(adjList)
        
        visited = set()
        
        def dfs(i):
            visited.add(i)
            for j in adjList[i]:
                if j not in visited:
                    dfs(j)
                
            
        
        
        
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        
        return count
