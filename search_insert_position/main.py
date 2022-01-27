"""
Description:

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
----------
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
----------
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution(object):
    def searchInsert(self, nums, target) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return left


# Simple test case
if __name__ == "__main__":

    target = 5
    nums = [1, 2, 3, 4, 5]
    solution = Solution()

    result = solution.searchInsert(nums, target)
    print(result)

    target_two = 7
    nums_two = [1, 2, 3, 4, 5, 6]

    result_two = solution.searchInsert(nums_two, target_two)
    print(result_two)
