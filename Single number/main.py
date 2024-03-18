class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
        
        
        
solution = Solution()

# Take input from the user
arr = input("Enter an array  : ")
array = []
for i in range(len(arr)):
    array.append(int(arr[i]))
          
result = solution.singleNumber(array)

# Print the result
print(result)


