class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize two pointers
        left = 0
        for right in range(len(nums)):
            # If the current element is not equal to val
            if nums[right] != val:
                # Swap the elements at left and right pointers
                nums[left] = nums[right]
                # Move the left pointer forward
                left += 1
        
        # The value of left is the number of elements not equal to val
        return left

if __name__ == "__main__":
    # Test cases
    solution = Solution()
    
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print("Output:", k1, "nums =", nums1[:k1])
    
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print("Output:", k2, "nums =", nums2[:k2])
