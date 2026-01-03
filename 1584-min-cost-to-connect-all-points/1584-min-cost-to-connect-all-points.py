class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size
        
        for i in range(size):
            self.group[i] = i
      
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        allEdges = []

        for currnode in range(n):
            for nextnode in range(currnode+1, n):
                weight = abs(points[currnode][0] - points[nextnode][0]) +\
                         abs(points[currnode][1] - points[nextnode][1])
                allEdges.append((weight, currnode, nextnode))
        allEdges.sort()
        uf = UnionFind(n)
        mstcost, edgesused = 0, 0
        for w, n1, n2 in allEdges:
            if uf.join(n1, n2):
                mstcost+=w
                edgesused +=1
                if edgesused == n-1:
                    break
        return mstcost