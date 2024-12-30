import sys
from typing import List, Tuple

"""
Description: https://leetcode.com/problems/jump-game-ii
Time Complexity: O(n * m) where m is the maximum number of steps that can be taken from a given position
Space Complexity: O(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        dp = [sys.maxsize] * len(nums)

        dp[0] = 0

        for i in range(len(nums)):
            for step in range(1, nums[i] + 1):
                if i + step >= len(nums):
                    pos = len(nums) - 1
                    dp[pos] = min(dp[pos], dp[pos] + 1)
                else:
                    dp[i + step] = min(dp[i + step], dp[i] + 1)

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.jump([2, 3, 1, 1, 4]) == 2, "Test Case 1 Failed"
    assert solution.jump([2, 3, 0, 1, 4]) == 2, "Test Case 2 Failed"
