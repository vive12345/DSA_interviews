class Solution:
    def dijstra(self, signalRecAt, k, n):
        pq =[]
        heapq.heappush(pq,(0, k))
        signalRecAt[k]=0
        while pq:
            currtime, currnode = heapq.heappop(pq)
            if currtime > signalRecAt[currnode]:
                continue
            for traveltime, nextnode in self.adj[currnode]:
                newtime = currtime + traveltime
                if signalRecAt[nextnode] > newtime:
                    signalRecAt[nextnode]= newtime
                    heapq.heappush(pq, (newtime, nextnode))

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.adj = [[] for _ in range(n+1)]
        print(self.adj)
        for source, dest, time in times:
            self.adj[source].append((time, dest))
        signalRecAt = [math.inf]*(n+1)
        print(self.adj)
        self.dijstra(signalRecAt, k, n)
        ans = max(signalRecAt[1:])
        return -1 if math.isinf(ans) else int(ans)

        