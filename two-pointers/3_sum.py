from typing import List

"""
Description: https://leetcode.com/problems/3sum/description/
Time Complexity: O(n^2)
Space Complexity: O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        memo = {}
        result = []

        # because there are 2 pointers, there is no need to go over all elements, thus len(nums) -2
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]

                if current_sum == target:
                    if (nums[i], nums[low], nums[high]) not in memo:
                        result.append([nums[i], nums[low], nums[high]])
                        memo[(nums[i], nums[low], nums[high])] = True

                    low += 1
                elif current_sum > target:
                    high -= 1
                else:
                    low += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    res = solution.threeSum([-1, 0, 1, 2, -1, -4])

    expected = [[-1, -1, 2], [-1, 0, 1]]

    assert len(res) == len(expected), "Test len 1 Failed"

    for r in res:
        assert r in expected, "Test Case 1 Failed"
