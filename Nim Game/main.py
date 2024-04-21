class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

solution = Solution()

n = int(input("Enter number of stones: "))

res = solution.canWinNim(n)
print(res)