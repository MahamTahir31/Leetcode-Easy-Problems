class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        
        # Initialize index for the merged array
        p = m + n - 1
        
        # Merge nums1 and nums2 from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, add them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1) 

nums1 = [1]
m = 1
nums2 = []
n = 0

sol.merge(nums1, m, nums2, n)
print(nums1)  

nums1 = [0]
m = 0
nums2 = [1]
n = 1

sol.merge(nums1, m, nums2, n)
print(nums1)