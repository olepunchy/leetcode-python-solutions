from black import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input())

    solution = Solution()
    result = solution.two_sum(num_list, target)
    print(result)
