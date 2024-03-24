class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize two pointers
        slow = 0
        
        # Iterate through the array with the fast pointer
        for fast in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[fast] != nums[slow]:
                # Move the slow pointer forward
                slow += 1
                # Update the value at the slow pointer position
                nums[slow] = nums[fast]
        
        # Return the count of unique elements
        return slow + 1

def main():
    nums = [1, 1, 2]
    solution = Solution()
    k = solution.removeDuplicates(nums)
    print("Output:", k)
    print("nums:", nums[:k], end="")
    print(", _" * (len(nums) - k))

if __name__ == "__main__":
    main()
