class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        proviences = 0
        n = len(isConnected)
        visited = set()
        def dfs(city):
            visited.add(city)
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    dfs(neighbour)

        for i in range(n):
            #this i would be like city 0, 1 2... etc
            if i not in visited:
                proviences += 1
                dfs(i)
        return proviences