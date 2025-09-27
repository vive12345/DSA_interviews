class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows , cols = len(mat), len(mat[0])
        matrix = [[float("inf")] * cols for _ in range(rows)]
        dq = deque()
        dist = 0
        seen = set()
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    matrix[r][c] = 0
                    dq.append((r,c, dist))
                    seen.add((r, c))
        while dq:
            zr, zc, dist = dq.popleft()
            for dr,dc in direction:
                nr, nc = zr+dr, zc+dc
                if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in seen:
                    matrix[nr][nc] = dist+1
                    seen.add((nr, nc))
                    dq.append((nr, nc, dist+1))
        return matrix


        