class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        l, r = 2, num // 2
        while l <= r:
            mid = l + (r - l) // 2
            sqr = mid * mid
            
            if sqr == num:
                return True
            elif sqr < num:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

solution = Solution()

num1 = 16
num2 = 14

print("Is {} a perfect square? {}".format(num1, solution.isPerfectSquare(num1)))
print("Is {} a perfect square? {}".format(num2, solution.isPerfectSquare(num2)))