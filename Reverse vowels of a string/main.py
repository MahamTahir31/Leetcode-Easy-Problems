class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            elif s[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        
        return "".join(s)

solution = Solution()
input_str = "hello"
output_str = solution.reverseVowels(input_str)
print("Input:", input_str)
print("Output:", output_str)
