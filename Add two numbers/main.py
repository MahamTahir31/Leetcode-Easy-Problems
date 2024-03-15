class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        result = num1 + num2
        return result
        
solution = Solution()

# Take input from the user
n1 = int(input("Enter a number1: "))
n2 = int(input("Enter a number2: "))

result = solution.sum(n1, n2)

# Print the result
print("Sum of ",n1, " and ",n2," is: ", result)


