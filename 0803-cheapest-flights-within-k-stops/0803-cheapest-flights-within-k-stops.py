from collections import defaultdict, deque
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list: src -> [(dest, cost)]
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        # Initialize distance array
        dist = [math.inf] * n
        dist[src] = 0
        
        # BFS-like traversal (level = number of stops)
        q = deque([(src, 0)])
        stops = 0
        
        while stops <= k and q:
            sz = len(q)
            # Temporary distances for this level to avoid premature updates
            temp_dist = dist.copy()
            
            for _ in range(sz):
                node, cost_so_far = q.popleft()
                
                # Explore neighbors
                for nei, price in adj[node]:
                    new_cost = cost_so_far + price
                    if new_cost < temp_dist[nei]:
                        temp_dist[nei] = new_cost
                        q.append((nei, new_cost))
            
            # Update distances for next level
            dist = temp_dist
            stops += 1
        
        return -1 if dist[dst] == math.inf else dist[dst]
