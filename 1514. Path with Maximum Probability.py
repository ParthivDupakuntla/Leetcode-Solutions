# Dijkstra's implementation -> heap queue as a priority queue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
            
        max_prob = [0.0]*n
        max_prob[start_node] = 1.0
        
        pq = [(-1.0, start_node)]
        
        while pq:
            curr_prob, curr_node = heapq.heappop(pq)
            if curr_node == end_node:
                return -curr_prob
            for next_node, path_prob in graph[curr_node]:
                if -curr_prob*path_prob > max_prob[next_node]:
                    max_prob[next_node] = -curr_prob*path_prob
                    heapq.heappush(pq, (-max_prob[next_node], next_node))
        return 0.0
        
