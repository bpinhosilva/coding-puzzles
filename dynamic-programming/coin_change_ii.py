from typing import List

"""
Description: https://leetcode.com/problems/coin-change-ii
Time Complexity: O(n*amount)
Space Complexity: O(amount)
"""


class Solution:
    def solve(self, amount: int, coins: List[int]) -> int:
        return self.change(amount, coins)

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        # there is only 1 way to achieve 0 sum which is using no coins
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        # the total amount of ways to sum up to `sum`
        # array is indexed starting at 0
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.solve(5, [1, 2, 5]) == 4, "Test Case 1 Failed"
