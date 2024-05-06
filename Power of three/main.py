class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:  
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

obj = Solution()
n = int(input("Enter number: "))
res = obj.isPowerOfThree(n)
print(res)