from black import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        """
        Input: sorted list of numbers
        Output: sorted list of numbers squared
        """

        for index, _ in enumerate(nums):
            value = nums[index]
            nums[index] = value * value

        return sorted(nums)


if __name__ == "__main__":

    numbers = [-4, -1, 0, 3, 10]

    solution = Solution()

    result = solution.sorted_squares(numbers)
    print(result)

    numbers_two = [-7, -3, 2, 3, 11]
    result_two = solution.sorted_squares(numbers_two)
    print(result_two)
