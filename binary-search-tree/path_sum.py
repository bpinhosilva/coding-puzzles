from typing import Optional

from bst_utils import BstUtils
from tree_node import TreeNode

"""
Description: https://leetcode.com/problems/path-sum
Time Complexity: O(n) 
Space Complexity: O(1)
"""


class Solution:
    def do_pre_order(self, node: Optional[TreeNode], target_sum: int, current_sum: int = 0) -> bool:
        if not node.left and not node.right:
            current_sum += node.val

            if current_sum == target_sum:
                return True

        result = False

        if node.left:
            result = result or self.do_pre_order(node.left, target_sum, current_sum + node.val)
        if node.right:
            result = result or self.do_pre_order(node.right, target_sum, current_sum + node.val)

        return result

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = False

        if not root:
            return result

        result = self.do_pre_order(root, targetSum, 0)

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.hasPathSum(BstUtils.from_array([1, 2, 3]), 5) == False, "Test Case 1 Failed"
    assert solution.hasPathSum(BstUtils.from_array([]), 0) == False, "Test Case 2 Failed"
    assert solution.hasPathSum(BstUtils.from_array([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
                               22) == True, "Test Case 3 Failed"
