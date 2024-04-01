class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = 0
        for i in range(len(nums)+1):
            if i not in nums:
                missing = i
        return missing
        
        

sol = Solution()
    
# Test case 1
nums1 = [3, 0, 1]
print("Test Case 1:")
print("Input:", nums1)
print("Output:", sol.missingNumber(nums1))  # Expected output: 2
print()

# Test case 2
nums2 = [0, 1]
print("Test Case 2:")
print("Input:", nums2)
print("Output:", sol.missingNumber(nums2))  # Expected output: 2
print()

# Test case 3
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print("Test Case 3:")
print("Input:", nums3)
print("Output:", sol.missingNumber(nums3))  # Expected output: 8