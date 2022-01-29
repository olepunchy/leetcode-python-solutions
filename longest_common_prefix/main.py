"""
Description: 14. Longest Common Prefix

Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
----------

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:
----------

Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
 

Constraints:
------------

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""
from black import List


class Solution:
    def longest_common_prefix(self, strings: List[str]) -> str:
        prefix = []

        for char in zip(*strings):
            if len(set(char)) == 1:
                prefix.append(char[0])
            else:
                break

        return "".join(prefix)


if __name__ == "__main__":
    words = ["flower", "flow", "flight"]

    solution = Solution()
    result = solution.longest_common_prefix(words)

    print(f"Longest common prefix: {result}")
