import unittest
from typing import List

"""
Time Complexity: O(n * capacity)
Space Complexity: O(n * capacity)
"""


class Solution:
    # what is the time complexity of this
    def solve(self, v: List[int], w: List[int], n: int, capacity: int) -> int:
        """
        Remember arrays v and w are 0-indexed while 2-D array m has to include
        values from 0 to capacity, thus [0, capacity + 1) indexed.
        """

        m = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if w[i - 1] > j:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = max(m[i - 1][j], m[i - 1][j - w[i - 1]] + v[i - 1])

        return m[n][capacity]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_cases(self):
        cases = [
            ([5, 4, 3, 2], [4, 3, 2, 1], 4, 6, 9),
            ([1, 2, 3], [4, 5, 1], 3, 4, 3),
            ([300, 200, 400, 500], [2, 1, 5, 3], 4, 10, 1200)
        ]

        for case in cases:
            v, w, n, capacity, expected = case

            result = self.solution.solve(v, w, n, capacity)

            self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
