class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            if char not in char_to_word and word not in word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char
            elif char not in char_to_word or char_to_word[char] != word:
                return False
            elif word not in word_to_char or word_to_char[word] != char:
                return False
        
        return True

if __name__ == "__main__":
    pattern = "abba"
    s1 = "dog cat cat dog"
    s2 = "dog cat cat fish"
    s3 = "dog cat cat dog"
    
    solution = Solution()
    print(solution.wordPattern(pattern, s1))  # Output: True
    print(solution.wordPattern(pattern, s2))  # Output: False
    print(solution.wordPattern(pattern, s3))  # Output: False
