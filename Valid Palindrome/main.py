class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned_s == cleaned_s[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(solution.isPalindrome("race a car"))                      # Output: false
print(solution.isPalindrome(" "))                               # Output: true
