class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num_str = str(num)
            total = 0
            for digit in num_str:
                total += int(digit)
            num = total
        return num
          
        
solution = Solution()

# Take input from the user
n = int(input("Enter a number: "))
result = solution.addDigits(n)

# Print the result
print("Addition of  ", n ," is ", result)


