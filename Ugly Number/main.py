class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        
        return n == 1

if __name__ == "__main__":
    solution = Solution()
    n = int(input("enter number: "))
    result = solution.isUgly(n)
    print(result)
