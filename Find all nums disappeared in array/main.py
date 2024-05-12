class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        disappeared = []
        for i in range(n):
            if nums[i] > 0:
                disappeared.append(i + 1)
        
        return disappeared


nums1 = [4,3,2,7,8,2,3,1]
nums2 = [1,1]

solution = Solution()
print("Output for nums1:", solution.findDisappearedNumbers(nums1))
print("Output for nums2:", solution.findDisappearedNumbers(nums2))
