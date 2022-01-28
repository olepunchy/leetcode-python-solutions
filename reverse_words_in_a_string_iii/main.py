"""
Description:

Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.


Example 1:
---------

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
----------

Input: s = "God Ding"
Output: "doG gniD"
"""


class Solution:
    def reverse_words(self, a_string: str) -> str:
        # Split the input string by spaces into a new list
        words = a_string.split(" ")
        # Create a new emptry string for storage
        new_words = ""

        for word in words:
            # Reverse the word using Python slicing
            word = word[::-1]
            # Append the word with a space to new_words
            new_words += word + " "

        # Remove any remaining white space off the right side
        return new_words.rstrip()


if __name__ == "__main__":

    solution = Solution()

    sentence = "Let's take a LeetCode contest"

    print(f"Before: {sentence}")

    result = solution.reverse_words(sentence)

    print(f"After: {result}")
