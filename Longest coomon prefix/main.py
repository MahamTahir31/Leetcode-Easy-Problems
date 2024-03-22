class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  
        for i, char in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        return strs[0]  

    
solution = Solution()

# Take input from the user
array = ["flow", "flower", "flew"]
array2 = ["dog", "cat", "mouse"]
result1 = solution.longestCommonPrefix(array)
result2 = solution.longestCommonPrefix(array2)

# Print the result
print(result1)
print(result2)


