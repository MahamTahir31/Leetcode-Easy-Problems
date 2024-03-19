class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):  
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output  
    
solution = Solution()

# Take input from the user
target = int(input("Enter sum value: "))
arr = input("Enter an array  : ")
array = []
for i in range(len(arr)):
    array.append(int(arr[i]))
          
result = solution.twoSum(array, target)

# Print the result
print(result)


