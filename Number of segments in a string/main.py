class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

solution = Solution()
s = input("Enter string: ")
res = solution.countSegments(s)
print("Possible segments for string", s, " are: ", res)