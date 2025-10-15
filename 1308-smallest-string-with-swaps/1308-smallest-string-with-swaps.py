class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
      
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX]> self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY]>self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX]+=1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)
            
        groupVert = defaultdict()
        for vert in range(len(s)):
            root = uf.find(vert)
            if root not in groupVert:
                groupVert[root]=[]
            groupVert[root].append(vert)
        #this above creates a hashmap like this {0:[0,3], 1:[1,2]}
        
        smallestSwap = ['']*len(s)
        for nodes in groupVert.values():
            char = []
            for node in nodes:
                char.append(s[node])
            char.sort()
            for i in range(len(nodes)):
                smallestSwap[nodes[i]] = char[i]
        # this above would give [d,b] then we sort it [b,d] and reassign it to smallSwap = [b, , , d]
        # t2nd itr would give [c,a] then we sort it [a,c] and reassign it to smallSwap = [b,a,c,d]
        return ''.join(smallestSwap)
                   