import sys
from typing import List

"""
Description: https://leetcode.com/problems/coin-change
"""
class Solution:

    def solve(self, coins: List[int], sum: int) -> int:
        min_coins = [sys.maxsize for _ in range(sum + 1)]

        min_coins[0] = 0

        for coin_value in coins:
            for j in range(1, sum + 1):
                # if taking current coin (+1) and counting solution for previously computed
                # value (min_coins[j - coin_value]) produces a smaller amount of coins to sum up to j,
                # then store it as min_coins[j]
                if j >= coin_value and min_coins[j - coin_value] + 1 < min_coins[j]:
                    min_coins[j] = min_coins[j - coin_value] + 1

        return int(min_coins[sum]) if min_coins[sum] != sys.maxsize else -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.solve([1, 2, 5], 11) == 3, "Test Case 1 Failed"
    assert solution.solve([2], 3) == -1, "Test Case 2 Failed"
    assert solution.solve([1], 0) == 0, "Test Case 3 Failed"
    assert solution.solve([1, 3, 5], 11) == 3, "Test Case 4 Failed"
    assert solution.solve([1, 3, 5], 3) == 1, "Test Case 5 Failed"
    assert solution.solve([], 5) == -1, "Test Case 6 Failed"
    assert solution.solve([1, 3, 5], 5) == 1, "Test Case 7 Failed"
    assert solution.solve([1, 3, 5], 10) == 2, "Test Case 8 Failed"
    assert solution.solve([1, 3, 5], 8) == 2, "Test Case 9 Failed"
