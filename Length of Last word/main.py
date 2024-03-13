class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s.split()
        length = len(string[-1])
        return length

# Create an instance of the Solution class
solution = Solution()

# Take input from the user
user_input = input("Enter a string: ")

# Call the lengthOfLastWord function with the user input
result = solution.lengthOfLastWord(user_input)

# Print the result
print("Length of the last word:", result)


