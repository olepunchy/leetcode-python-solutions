"""
Description: 53. Max Subarray

"""
from black import List


def max_sub_array(self, nums: List[int]) -> int:
    # Set the current and max to the first element in nums
    current_sub = nums[0]
    max_sub = nums[0]

    for num in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise keep it
        current_sub = max(num, current_sub + num)

        # Set max to the maximum between our two tracking variables
        max_sub = max(max_sub, current_sub)

    return max_sub
