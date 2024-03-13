import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(math.sqrt(x))
        return res
        
solution = Solution()

# Take input from the user
user_input = int(input("Enter a number: "))

result = solution.mySqrt(user_input)

# Print the result
print("Square root of ",user_input," is: ", result)


