"""
Description: 20. Valid Parentheses
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
----------

Input: s = "()"
Output: true

Example 2:
---------

Input: s = "()[]{}"
Output: true

Example 3:
----------

Input: s = "(]"
Output: false
 

Constraints:
------------

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution:
    def is_valid(self, string: str) -> bool:

        opening = set("([{")

        matches = set([("(", ")"), ("[", "]"), ("{", "}")])

        stack = []

        for char in string:
            # Left Side:
            # If the character appears in the opening set, append it to the stack
            if char in opening:
                stack.append(char)

            # Right side:
            # The character is not part of the opening set
            else:
                # If there are no characters on the stack, it is not a match
                if len(stack) == 0:
                    return False

                # Look at the last thing pushed onto the stack
                last_char = stack.pop()

                # Check if this char and last_char are in the matches set
                if (last_char, char) not in matches:
                    return False

        # Everything should have been popped off the stack
        return len(stack) == 0


class SolutionTwo:
    def is_valid(self, string: str) -> bool:
        bracket_dict = {"(": ")", "[": "]", "{": "}"}
        opening = set(["[", "(", "{"])

        stack = []

        for char in string:
            # char is in opening
            if char in opening:
                # push char onto the stack
                stack.append(char)

            # char is not in opening, see if the last element in stack is in the dict
            elif stack and char == bracket_dict[stack[-1]]:
                # pop char off the stack
                stack.pop()

            # not found, return false
            else:
                return False

        # stack will be empty if everything was a match
        return stack == []


class SolutionThree:
    def is_valid(self, string: str) -> bool:
        # stack for tracking opening brackets
        stack = []

        # dictionary for keeping track of mappings
        brackets = {")": "(", "}": "{", "]": "["}

        for char in string:
            # if char is a closing bracket
            if char in brackets:
                # pop the top element on the stack
                top = stack.pop() if stack else "#"

                # the top element is not a value in brackets
                if brackets[char] != top:
                    return False

            # char is not a closing bracket
            else:
                # add it to the stack
                stack.append(char)

        return stack == []
