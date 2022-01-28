"""
Description:

Write a function that reverses a string. The input string is given as an array
of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:
---------

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
----------

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from black import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        low = 0
        high = len(s) - 1

        while low < high:
            left = s[low]
            right = s[high]

            s[low] = right
            s[high] = left

            low += 1
            high -= 1


if __name__ == "__main__":

    solution = Solution()

    test_string = ["h", "e", "l", "l", "o"]

    print(f"Before reverse: {test_string}")

    solution.reverse_string(test_string)

    print(f"After reverse: {test_string}")
