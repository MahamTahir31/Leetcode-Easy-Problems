class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums

if __name__ == "__main__":
    solution = Solution()
    n = [1, 0, 2,0, 3, 4]
    result = solution.moveZeroes(n)
    print("all zeros shifted to right: ", result)
