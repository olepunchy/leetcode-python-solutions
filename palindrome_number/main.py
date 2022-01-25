class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_string = str(x)

        reversed_string = ""

        index = len(x_string) - 1

        while index >= 0:
            reversed_string += x_string[index]
            index -= 1

        return x_string == reversed_string
