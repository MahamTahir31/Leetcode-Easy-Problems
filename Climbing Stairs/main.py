class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b

        
n = int(input("Enter Number: "))

solution = Solution()

result = solution.climbStairs(n)

print("The possible steps are :", result)