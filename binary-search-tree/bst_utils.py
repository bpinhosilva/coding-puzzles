import unittest

from tree_node import TreeNode


class BstUtils:
    @staticmethod
    def from_array(array: list[int]) -> TreeNode:
        if not array:
            return None

        root = TreeNode(array[0])
        queue = [root]
        i = 1

        while i < len(array):
            current = queue.pop(0)

            if i < len(array) and array[i] is not None:
                current.left = TreeNode(array[i])
                queue.append(current.left)

            i += 1

            if i < len(array) and array[i] is not None:
                current.right = TreeNode(array[i])
                queue.append(current.right)

            i += 1

        return root


class TestSolution(unittest.TestCase):

    def test_cases(self):
        cases = [
            (1, [5, 4, 8])
        ]

        for case in cases:
            n, input = case

            tree = BstUtils.from_array(input)

            self.assertIsNotNone(tree)
            self.assertEqual(5, tree.val)
            self.assertEqual(4, tree.left.val)
            self.assertEqual(8, tree.right.val)


if __name__ == "__main__":
    unittest.main()
