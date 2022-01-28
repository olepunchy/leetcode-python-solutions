from black import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array in place

        Runtime: O(n), we will have to look at each element in nums
        Space: O(n), we will be creating a new working list the same size

        Input: a list of numbers
        Output: None, change the order in palce
        """

        # Create a new list filled with zeros that is the same length as nums
        length = len(nums)
        new_nums = [0] * len(nums)

        for i in range(len(nums)):
            # The index in new_nums will be i + k % length.
            # For example:
            # i = 0, k = 2, length = 6
            # 0 + 2 = 2
            # 2 % 6 = 2
            # The value at nums[0] would be placed at nums[2]
            new_nums[(i + k) % length] = nums[i]

        # Replace nums with new_nums
        nums[:] = new_nums


# Simple test
if __name__ == "__main__":

    solution = Solution()

    arr = [1, 2, 3, 4, 5, 6]
    rotate_amount = 2

    print(f"Original list: {arr}")

    solution.rotate(arr, rotate_amount)

    print(f"Altered list: {arr}")
