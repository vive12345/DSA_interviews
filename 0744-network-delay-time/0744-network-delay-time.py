from collections import defaultdict
import math

class Solution:
    def __init__(self):
        self.adj = defaultdict(list)

    def dfs(self, signalReceivedAt, currNode, currTime):
        # If current path is already slower than known best, skip
        if currTime >= signalReceivedAt[currNode]:
            return

        # Record faster arrival time
        signalReceivedAt[currNode] = currTime

        # No outgoing edges → stop
        if currNode not in self.adj:
            return

        # Explore neighbors
        for travelTime, neighbor in self.adj[currNode]:
            self.dfs(signalReceivedAt, neighbor, currTime + travelTime)

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list
        for u, v, w in times:
            self.adj[u].append((w, v))

        # Sort each adjacency list by travel time (smallest first)
        for node in self.adj:
            self.adj[node].sort(key=lambda x: x[0])

        # Initialize signal times
        signalReceivedAt = [math.inf] * (n + 1)

        # Run DFS from source
        self.dfs(signalReceivedAt, k, 0)

        # Compute result
        answer = max(signalReceivedAt[1:])
        return -1 if answer == math.inf else answer
