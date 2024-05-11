class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float('-inf')  # Initialize three variables to store the top three maximum numbers

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num < first and num > second:
                third = second
                second = num
            elif num < second and num > third:
                third = num

        # Check if the third maximum exists or not
        if third != float('-inf'):
            return third
        else:
            return first  # If the third maximum doesn't exist, return the first maximum


solution = Solution()
print(solution.thirdMax([3, 2, 1]))  # Output: 1
print(solution.thirdMax([1, 2]))  # Output: 2
print(solution.thirdMax([2, 2, 3, 1]))  # Output: 1
