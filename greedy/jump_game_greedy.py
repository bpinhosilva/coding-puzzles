from typing import List

"""
Description: https://leetcode.com/problems/jump-game
Time Complexity: O(n)
Space Complexity: O(1) -> max_position_index single variable
"""


class Solution:
    def greedy_solution(self, nums: List[int]) -> bool:

        # the maximum index position reached so far
        max_position_index = 0

        for i in range(len(nums)):
            # if position is greater than the current max position
            if i > max_position_index:
                return False

            max_position_index = max(max_position_index, i + nums[i])

            if max_position_index >= len(nums) - 1:
                return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.greedy_solution(nums)


if __name__ == "__main__":
    solution = Solution()

    assert solution.canJump([2, 3, 1, 1, 4]) == True, "Test Case 1 Failed"
    assert solution.canJump([3, 2, 1, 0, 4]) == False, "Test Case 2 Failed"
    assert solution.canJump([1]) == True, "Test Case 3 Failed"
    assert solution.canJump([0, 3, 1, 1, 4]) == False, "Test Case 4 Failed"
    assert solution.canJump([1, 0, 1, 0]) == False, "Test Case 5 Failed"
    assert solution.canJump([3, 0, 8, 2, 0, 0, 1]) == True, "Test Case 6 Failed"
