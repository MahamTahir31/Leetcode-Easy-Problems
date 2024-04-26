class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


nums1 = [1, 2, 3, 1]
solution = Solution()
print("Example 1:", solution.containsDuplicate(nums1))  # Output: True

nums2 = [1, 2, 3, 4]
print("Example 2:", solution.containsDuplicate(nums2))  # Output: False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print("Example 3:", solution.containsDuplicate(nums3))  # Output: True
