import heapq
import math
from collections import defaultdict

class Solution:
    def __init__(self):
        self.adj = defaultdict(list)

    def dijkstra(self, signalReceivedAt, source):
        pq = []
        heapq.heappush(pq, (0, source))  # (time, node)
        signalReceivedAt[source] = 0

        while pq:
            currTime, currNode = heapq.heappop(pq)

            # Skip if we already found a faster route
            if currTime > signalReceivedAt[currNode]:
                continue

            # Explore neighbors
            for time, neighbor in self.adj[currNode]:
                newTime = currTime + time
                if newTime < signalReceivedAt[neighbor]:
                    signalReceivedAt[neighbor] = newTime
                    heapq.heappush(pq, (newTime, neighbor))

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list
        for u, v, w in times:
            self.adj[u].append((w, v))

        # Initialize signal times
        signalReceivedAt = [math.inf] * (n + 1)

        # Run Dijkstra from source k
        self.dijkstra(signalReceivedAt, k)

        # Compute answer
        answer = max(signalReceivedAt[1:])  # ignore index 0

        return -1 if answer == math.inf else answer
