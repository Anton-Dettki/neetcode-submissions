from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()

        for i in range(rows):
            for j in range(cols):

                if board[i][j] == 'O' and (i, j) not in visited:

                    region = []
                    touches_border = False

                    queue = deque([(i, j)])
                    visited.add((i, j))

                    while queue:
                        x, y = queue.popleft()

                        region.append((x, y))

                        # Check if current cell touches the border
                        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                            touches_border = True

                        # Explore neighbors
                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy

                            if 0 <= nx < rows and 0 <= ny < cols:
                                if board[nx][ny] == 'O' and (nx, ny) not in visited:

                                    visited.add((nx, ny))
                                    queue.append((nx, ny))

                    # Capture the entire region if it doesn't touch the border
                    if not touches_border:
                        for x, y in region:
                            board[x][y] = 'X'

        return