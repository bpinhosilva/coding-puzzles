"""
Description: https://leetcode.com/problems/unique-paths
Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (m == n and m == 1):
            return 1

        w, h = n, m
        arr = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(n):
            arr[0][i] = 1

        for i in range(1, m):
            for j in range(n):
                arr[i][j] = arr[i][j - 1] + arr[i - 1][j]

        return arr[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()

    assert solution.uniquePaths(3, 7) == 28, "Case 1 failed"
    assert solution.uniquePaths(3, 2) == 3, "Case 2 failed"
