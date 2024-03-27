class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        output = 0
        if target in nums:
                output = nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] < target:
                    output = i + 1
                        
        return output


solution = Solution()

# Example 1
nums1 = [1,3,5,6]
target1 = 5
print(f"Example 1:\nInput: nums = {nums1}, target = {target1}\nOutput: {solution.searchInsert(nums1, target1)}")

# Example 2
nums2 = [1,3,5,6]
target2 = 2
print(f"\nExample 2:\nInput: nums = {nums2}, target = {target2}\nOutput: {solution.searchInsert(nums2, target2)}")

# Example 3
nums3 = [1,3,5,6]
target3 = 7
print(f"\nExample 3:\nInput: nums = {nums3}, target = {target3}\nOutput: {solution.searchInsert(nums3, target3)}")


    