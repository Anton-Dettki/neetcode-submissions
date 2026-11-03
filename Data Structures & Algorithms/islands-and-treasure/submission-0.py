class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        1. Initialize a queue with all treasure chests.
        2. Process the queue using popleft().
            3. Explore the four directions.
            4. Check boundaries.
            5. Only visit cells whose value is INF.
            6. Assign their distance and enqueue them.
        """

        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        queue = deque()
        # Init a queue with all treasure chests
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] == 2147483647:
                            queue.append((nx, ny))
                            grid[nx][ny] = steps
        return
        


