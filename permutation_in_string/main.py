"""
Description: 567. Permutation in String
Difficulty: Medium
"""


from collections import Counter


class Solution:
    def check_inclusion(self, sub_string: str, main_string: str) -> bool:

        sub_string_length = len(sub_string)

        sub_string_map = Counter(sub_string)

        for i in range(len(main_string) - sub_string_length + 1):
            main_string_map = main_string[i : i + sub_string_length]
            if sub_string_map == Counter(main_string_map):
                return True

        return False
