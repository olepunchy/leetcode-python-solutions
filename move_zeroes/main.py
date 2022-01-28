"""
Description:

Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:
---------

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
---------

Input: nums = [0]
Output: [0]
"""
from black import List


class Solution:
    """
    Solution implementation for the Move Zeroes problem on leetcode.com
    """

    def __init__(self):
        self.name = "Solution"

    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Create a new list filled with zeroes of the same length as nums
        length = len(nums)
        new_nums = [0] * length

        insert_index = 0

        for i in range(length):
            if nums[i] != 0:
                # Insert the number towards the beginning of the list
                new_nums.insert(insert_index, nums[i])
                # The list is now one larger, pop an element off the back
                new_nums.pop()
                # Increment the index for insertion
                insert_index += 1

        nums[:] = new_nums


if __name__ == "__main__":
    solution = Solution()

    numbers = [0, 1, 0, 3, 12]

    print(f"Before: {numbers}")

    solution.move_zeroes(numbers)

    print(f"After: {numbers}")
