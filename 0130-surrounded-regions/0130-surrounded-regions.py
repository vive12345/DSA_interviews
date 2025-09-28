class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dq = deque()
        seen = set()
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows-1 or col == 0 or col == cols-1) and board[row][col] == 'O':
                    dq.append((row, col))
                    seen.add((row, col))
        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and board[nr][nc] == 'O':
                    seen.add((nr, nc))
                    dq.append((nr, nc))
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='O' and (row, col) not in seen :
                    seen.add((row, col))
                    board[row][col]='X' 