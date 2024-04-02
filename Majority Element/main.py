
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxNum = 0
        for i in range(len(nums)):
            if count == 0:
                maxNum = nums[i]
            if (maxNum == nums[i]):
                count+=1
            else:
                count-=1
        return maxNum
              
        

solution = Solution()
    
nums1 = [1, 2, 2, 3, 2]
print("Majority element:", solution.majorityElement(nums1))  # Output: 2

nums2 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Majority element:", solution.majorityElement(nums2))  # Output: 4