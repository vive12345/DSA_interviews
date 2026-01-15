class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        used_edges = 0
        mst_cost = 0
        in_mst=[False]*n
        heap = [(0,0)] # weight, nodeobject
        while used_edges < n:
            weight, curr_node = heapq.heappop(heap)
            if in_mst[curr_node]:
                continue
            in_mst[curr_node]= True
            used_edges+=1
            mst_cost+=weight
            for nextnode in range(n):
                if not in_mst[nextnode]:
                    next_weight = abs(points[curr_node][0] - points[nextnode][0]) +\
                    abs(points[curr_node][1] - points[nextnode][1])
                    heapq.heappush(heap,(next_weight, nextnode))
        return mst_cost