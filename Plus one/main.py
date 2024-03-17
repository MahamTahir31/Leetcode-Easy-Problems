class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ""
        for i in digits:
            a+=str(i)
            b = int(a)+1
        c = []
        for j in str(b):
            c.append(int(j))
        return c
        
        
solution = Solution()

# Take input from the user
arr = input("Enter an array  : ")
array = []
for i in range(len(arr)):
    array.append(int(arr[i]))
          
result = solution.plusOne(array)

# Print the result
print(result)


