"""
Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:
* 1 <= nums.length <= 104
* -104 < nums[i], target < 104
* All the integers in nums are unique.
* nums is sorted in ascending order.
"""
from black import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Assume the list is sorted in ascending order (low to high)
        # Return the index of the target if found, or -1 if not found
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        return -1


if __name__ == '__main__':
    target = int(input("Target number: "))
    num_list = [-1, 0, 3, 5, 9, 12]

    solution = Solution()
    result = solution.search(num_list, target)
    print(result)
