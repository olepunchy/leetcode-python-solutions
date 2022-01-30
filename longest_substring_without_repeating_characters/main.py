"""
Description: 3. Longest Substring Without Repeating Characters
Difficulty: Medium
"""

"""
Sliding window approach

Time complexity: O(2n)
Space complexity: O(min(m, n))
"""


class Solution:
    def length_of_longest_substring(self, the_string: str) -> int:
        chars = [0] * 128

        left = right = 0

        result = 0

        while right < len(the_string):
            r = the_string[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = the_string[left]
                chars[ord(l)] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result


class SolutionTwo:
    """
    Time complexity: O(n)
    Space complexity: O(min(m, n))
    """

    def length_of_longest_substring(self, the_string: str) -> int:
        chars = [None] * 128

        left = right = 0

        result = 0

        while right < len(the_string):
            r = the_string[right]

            index = chars[ord(r)]

            if index != None and index >= left and index < right:
                left = index + 1

            result = max(result, right - left + 1)

            chars[ord(r)] = right
            right += 1

        return result


class SolutionThree:
    def length_of_longest_substring(self, the_string: str) -> int:
        """
        :type the_string: str
        :return: int
        """
        result = 0
        substring = ""

        for char in the_string:
            if char not in substring:
                substring += char
                result = max(result, len(substring))
            else:
                cut = substring.index(char)
                substring = substring[cut + 1 :] + char

        return result
