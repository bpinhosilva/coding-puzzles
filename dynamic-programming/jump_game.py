from typing import List

"""
Description: https://leetcode.com/problems/jump-game
Time Complexity: O(n)
Space Complexity: O(n)
Alternative greedy solution at ../greedy/jump_game_greedy.py
"""


class Solution:
    def has_reached_end(self, nums, visited):
        return len(nums) - 1 in visited

    def do_dfs(self, index, nums, visited={}):
        if index in visited:
            return

        # if jump is greater than the length of the array
        # it's still valid
        if index >= len(nums) - 1:
            visited[len(nums) - 1] = True
            return

        for i in range(nums[index], 0, -1):
            if self.has_reached_end(nums, visited):
                return

            self.do_dfs(index + i, nums, visited)

        # mark as visited after reaching all possible paths from it
        visited[index] = True

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        visited = {}

        self.do_dfs(0, nums, visited)

        return self.has_reached_end(nums, visited)


if __name__ == "__main__":
    solution = Solution()

    assert solution.canJump([2, 3, 1, 1, 4]) == True, "Test Case 1 Failed"
    assert solution.canJump([3, 2, 1, 0, 4]) == False, "Test Case 2 Failed"
    assert solution.canJump([1]) == True, "Test Case 3 Failed"
    assert solution.canJump([0, 3, 1, 1, 4]) == False, "Test Case 4 Failed"
    assert solution.canJump([1, 0, 1, 0]) == False, "Test Case 5 Failed"
    assert solution.canJump([3, 0, 8, 2, 0, 0, 1]) == True, "Test Case 6 Failed"
