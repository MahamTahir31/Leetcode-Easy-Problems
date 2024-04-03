class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        x = 0
        while 2**x <= n:
            if 2**x == n:
                return True
            x += 1
        
        return False

# Example usage:
solution = Solution()
print(solution.isPowerOfTwo(1))  # Output: true
print(solution.isPowerOfTwo(16)) # Output: true
print(solution.isPowerOfTwo(3))  # Output: false
