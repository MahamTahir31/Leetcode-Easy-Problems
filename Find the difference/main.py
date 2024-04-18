class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
    
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return char
        
        for char, freq in count.items():
            if freq != 0:
                return char

solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
print(solution.findTheDifference("", "y"))         # Output: "y"
