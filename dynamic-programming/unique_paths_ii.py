from typing import List, Tuple

"""
Description: https://leetcode.com/problems/unique-paths-ii
Time Complexity: O(m*n)
"""

# Need to be careful with limits and corner cases
class Solution:
    def is_valid(self, point: Tuple, grid: List[List[int]]):
        r, c = point
        return grid[r][c] == 0

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid

        if g[0][0] == 1:
            return 0

        rows = len(g)
        cols = len(g[0])

        # the solution grip to build up the final solution
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        # fill out 1st line
        for j in range(cols):
            if self.is_valid((0, j), g):
                dp[0][j] = 1
            else:
                # it cannot proceed because there's an obstacle
                break

        # fill out 1st colum excluding item [0][0]
        for i in range(1, rows):
            if self.is_valid((i, 0), g):
                dp[i][0] = 1
            else:
                # it cannot proceed because there's an obstacle
                break

        for i in range(1, rows):
            for j in range(1, cols):
                # only compute if the current position is not an obstacle
                if self.is_valid((i, j), g):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        res = dp[rows - 1][cols - 1]

        return res


if __name__ == "__main__":
    solution = Solution()

    assert solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2, "Test Case 1 Failed"
    assert solution.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1, "Test Case 2 Failed"
    assert solution.uniquePathsWithObstacles([[0]]) == 1, "Test Case 3 Failed"
    assert solution.uniquePathsWithObstacles([[1]]) == 0, "Test Case 4 Failed"
    assert solution.uniquePathsWithObstacles([[1, 0]]) == 0, "Test Case 5 Failed"
    assert solution.uniquePathsWithObstacles([[0], [0]]) == 1, "Test Case 6 Failed"
