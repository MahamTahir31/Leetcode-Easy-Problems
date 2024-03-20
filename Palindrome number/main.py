class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        return x_str == x_str[::-1]

    
solution = Solution()

# Take input from the user
num = int(input("Enter number: "))
     
result = solution.isPalindrome(num)

# Print the result
print(result)


