from typing import Optional

from bst_utils import BstUtils
from tree_node import TreeNode

"""
Description: https://leetcode.com/problems/sum-of-left-leaves
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def do_post_order(self, node: TreeNode, is_left_child=False) -> int:
        if not node.left and not node.right and is_left_child:
            return node.val

        total_left = self.do_post_order(node.left, True) if node.left else 0
        total_right = self.do_post_order(node.right, False) if node.right else 0

        return total_left + total_right

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.do_post_order(root, False)


if __name__ == "__main__":
    solution = Solution()

    root = BstUtils.from_array([3, 9, 20, None, None, 15, 7])

    res = solution.sumOfLeftLeaves(root)

    assert res == 24, "Test Case 1 Failed"
