class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
    
        # Count the occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Find the first unique character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        # If no unique character found
        return -1
solution = Solution()
print(solution.firstUniqChar("leetcode"))      # Output: 0
print(solution.firstUniqChar("loveleetcode"))   # Output: 2
print(solution.firstUniqChar("aabb"))           # Output: -1