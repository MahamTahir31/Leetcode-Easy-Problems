class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            if num in nums2 and num not in res:
                res.append(num)
        return res

  
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
print("Example 1:")
print("Input:", nums1, nums2)
print("Output:", sol.intersection(nums1, nums2))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print("\nExample 2:")
print("Input:", nums1, nums2)
print("Output:", sol.intersection(nums1, nums2))
