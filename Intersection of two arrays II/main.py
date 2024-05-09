class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        res = []
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
print("Example 1:")
print("Input:", nums1, nums2)
print("Output:", sol.intersect(nums1, nums2))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print("\nExample 2:")
print("Input:", nums1, nums2)
print("Output:", sol.intersect(nums1, nums2))
