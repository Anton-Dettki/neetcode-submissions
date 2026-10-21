class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = 0

        directions = [(-1, 0), (1, 0),(0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    curr = 1
                    queue = deque([(r,c)])
                    grid[r][c] = 0


                    while queue:

                        rr,cc = queue.popleft()

                        for dr, dc in directions:
                            nr = rr + dr
                            nc = cc + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                curr += 1
                                queue.append((nr,nc))
                                grid[nr][nc] = 0
                            res = max(curr, res)

        return res


