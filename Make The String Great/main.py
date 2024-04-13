class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                # Pop the previous character if it forms a bad pair
                stack.pop()
            else:
                # Push the character to the stack
                stack.append(char)

        # Return the string formed from the remaining characters
        return ''.join(stack)


# Main program for demonstration
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s = "leEeetcode"
    result = solution.makeGood(s)
    print(f"Input: {s}, Output: {result}")  # Output: Input: leEeetcode, Output: leetcode

    # Example 2
    s = "abBAcC"
    result = solution.makeGood(s)
    print(f"Input: {s}, Output: {result}")  # Output: Input: abBAcC, Output: 

    # Example 3
    s = "s"
    result = solution.makeGood(s)
    print(f"Input: {s}, Output: {result}")  # Output: Input: s, Output: s
