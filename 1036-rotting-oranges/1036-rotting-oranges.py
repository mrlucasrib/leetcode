from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j, 0))

        while queue:
            ni, nj, nk = queue.popleft()
            print(grid, ni, nj, nk)

            for i, j, k in [
                (ni + 1, nj, nk),
                (ni - 1, nj, nk),
                (ni, nj + 1, nk),
                (ni, nj - 1, nk),
            ]:
                if (
                    self.in_bounds(i, j, grid)
                    and grid[i][j] not in visited
                    and grid[i][j] == 1
                ):
                    queue.append((i, j, k + 1))
                    visited.add((i, j, k + 1))
                    grid[i][j] = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        maxK = 0
        for i, j, k in visited:
            maxK = max(maxK, k)
        return maxK

    def in_bounds(self, i, j, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            return True
        return False
