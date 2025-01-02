from typing import Optional

from bst_utils import BstUtils
from tree_node import TreeNode

"""
Description: https://leetcode.com/problems/path-sum-ii
Time Complexity: O(n) 
Space Complexity: O(n)
"""


class Solution:
    def do_pre_order(self, node: Optional[TreeNode], target_sum: int, path: list[int], result: list[list[int]]) -> None:
        if not node.left and not node.right:
            path.append(node.val)

            if sum(path) == target_sum:
                result.append(path[:])

            return

        path.append(node.val)

        if node.left:
            self.do_pre_order(node.left, target_sum, path[:], result)
        if node.right:
            self.do_pre_order(node.right, target_sum, path[:], result)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        result = []

        if not root:
            return result

        self.do_pre_order(root, targetSum, [], result)

        return result


if __name__ == "__main__":
    solution = Solution()

    result = solution.pathSum(BstUtils.from_array([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22)

    print(result)
