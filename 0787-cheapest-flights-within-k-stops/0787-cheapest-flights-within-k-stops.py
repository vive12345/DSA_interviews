from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0

        # Run exactly k+1 relaxations (paths with up to k+1 edges i.e., k stops)
        for _ in range(k + 1):
            temp = dist[:]  # copy
            for u, v, w in flights:
                if dist[u] != math.inf:
                    temp[v] = min(temp[v], dist[u] + w)
            dist = temp

        return -1 if dist[dst] == math.inf else dist[dst]
