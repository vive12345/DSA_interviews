class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dq = deque()
        seen = set()
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # top and bottom rows
        for col in range(cols):
            if board[0][col] == 'O':
                dq.append((0, col))
                seen.add((0, col))
            if board[rows-1][col] == 'O':
                dq.append((rows-1, col))
                seen.add((rows-1, col))

        # left and right columns
        for row in range(rows):
            if board[row][0] == 'O':
                dq.append((row, 0))
                seen.add((row, 0))
            if board[row][cols-1] == 'O':
                dq.append((row, cols-1))
                seen.add((row, cols-1))

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
