class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        Total = len(candyType) // 2  
        return min(len(set(candyType)), Total)


candyType1 = [1, 1, 2, 2, 3, 3]
candyType2 = [1, 1, 2, 3]
candyType3 = [6, 6, 6, 6]

solution = Solution()
print("Example 1:", solution.distributeCandies(candyType1))  # Output: 3
print("Example 2:", solution.distributeCandies(candyType2))  # Output: 2
print("Example 3:", solution.distributeCandies(candyType3))  # Output: 1
