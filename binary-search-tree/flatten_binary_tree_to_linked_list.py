from typing import Optional

from bst_utils import BstUtils
from tree_node import TreeNode

"""
Description: https://leetcode.com/problems/path-sum
Time Complexity: O(n) 
"""


class Solution:
    def do_pre_order(self, node: Optional[TreeNode]) -> TreeNode:

        left_side = None
        right_side = None

        if node.left:
            left_side = self.do_pre_order(node.left)

        if node.right:
            right_side = self.do_pre_order(node.right)

        if left_side:
            node.right = left_side
            node.left = None

        if right_side and left_side:
            # if left side is not present, the right side is already correct, do nothing
            # where to append
            temp_node = node

            while temp_node.right:
                temp_node = temp_node.right

            temp_node.right = right_side
            temp_node.left = None

        return node

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            self.do_pre_order(root)


if __name__ == "__main__":
    solution = Solution()

    root = BstUtils.from_array([1, 2, 5, 3, 4, None, 6])

    solution.flatten(root)

    assert root.val == 1
    assert root.left is None
    assert root.right.val == 2
    assert root.right.left is None
    assert root.right.right.val == 3
