from typing import List

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        
        graph = {i: [] for i in range(n)}
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        self.min_cost = float('inf')
        
        # DFS
        def dfs(city, time, cost):
            # Verifica se atingimos o destino e se o tempo é aceitável
            if city == n - 1 and time <= maxTime:
                self.min_cost = min(self.min_cost, cost)
                return
            if time > maxTime:
                return
            
            # Explorar cada cidade vizinha
            for neighbor, travel_time in graph[city]:
                dfs(neighbor, time + travel_time, cost + passingFees[neighbor])
        
        dfs(0, 0, passingFees[0])
        
        return self.min_cost if self.min_cost != float('inf') else -1
