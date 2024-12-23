import unittest

"""
Description: https://leetcode.com/problems/generate-parentheses
"""


class TestSolution(unittest.TestCase):

    def test_cases(self):
        solution = Solution()

        cases = [
            (1, ['()']),
            (3, ['((()))', '(()())', '(())()', '()(())', '()()()'])
        ]

        for case in cases:
            n, expected = case

            result = solution.solve(n)

            for exp in expected:
                self.assertIn(exp, result)


class Solution:
    def do_it(self, n_open, n_close, str="", results=[]):
        if n_open == 0 and n_close == 0:
            results.append(str)
            return
            # n_open > n_close means that at some point, a closing parenthesis came
            # before an opening parenthesis, and this is an invalid state.
        elif n_open < 0 or n_open > n_close:
            return
        else:
            self.do_it(n_open - 1, n_close, str + "(", results)
            self.do_it(n_open, n_close - 1, str + ")", results)

    def solve(self, n):
        results = []

        self.do_it(n, n, "", results)

        return results


if __name__ == "__main__":
    unittest.main()
