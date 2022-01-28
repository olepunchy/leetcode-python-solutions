"""
Description:

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
order, find two numbers such that they add up to a specific target number.

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.


Example 1:
---------
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


Example 2:
---------
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
---------
Input: numbers = [-1,0], target = -1
Output: [1,2]

Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
from black import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        """
        Binary search implementation
        """
        low = 0
        high = len(numbers) - 1

        while low < high:
            # Add the low and high numbers
            num = numbers[low] + numbers[high]

            # If num is equal to the target, found the indexes to return
            if num == target:
                # Add 1 to account for a 1-indexed answer
                return [low + 1, high + 1]

            # If num is lower than the target, increse low by 1
            elif num < target:
                low += 1
            # num is higher than the target, decrease by 1
            else:
                high -= 1


# Simple class test
if __name__ == "__main__":

    solution = Solution()

    numbers_list = [2, 7, 11, 15]
    target_num = 9

    result = solution.two_sum(numbers_list, target_num)
    # Correct output would be [1, 2], the first (2) and second element (7) = 9
    print(f"Result: {result}")
