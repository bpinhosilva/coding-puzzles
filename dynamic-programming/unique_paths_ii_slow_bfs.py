from typing import List, Tuple


# Slow solution using BFS
class Solution:
    def is_valid_path(self, point: Tuple, grid: List[List[int]]):
        rows = len(grid)
        cols = len(grid[0])

        r, c = point

        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        counter = 0

        steps = [(0, 1), (1, 0)]
        g = obstacleGrid

        rows = len(g)
        cols = len(g[0])

        q = []

        if g[0][0] == 0:
            q.append((0, 0))

        while len(q) > 0:
            r, c = q.pop(0)

            # is it the final position?
            if r == rows - 1 and c == cols - 1:
                if g[r][c] == 1:
                    break

                counter = counter + 1
                continue

            for s in steps:
                next_r = r + s[0]
                next_c = c + s[1]

                if self.is_valid_path((next_r, next_c), g):
                    q.append((next_r, next_c))

        return counter


if __name__ == "__main__":
    solution = Solution()

    assert solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2, "Test Case 1 Failed"
    assert solution.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1, "Test Case 2 Failed"
    assert solution.uniquePathsWithObstacles([[0]]) == 1, "Test Case 3 Failed"
    assert solution.uniquePathsWithObstacles([[1]]) == 0, "Test Case 4 Failed"
    assert solution.uniquePathsWithObstacles([[1, 0]]) == 0, "Test Case 5 Failed"
    assert solution.uniquePathsWithObstacles([[0], [0]]) == 1, "Test Case 6 Failed"
