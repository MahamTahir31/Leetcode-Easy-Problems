class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        a = word
        if a == word.capitalize():
            return True
        elif a== word.upper():
            return True
        elif a == word.lower():
            return True

        return False
solution = Solution()
s = input("Enter word: ")
res = solution.detectCapitalUse(s)
print(res)