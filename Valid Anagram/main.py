class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False

    char_count = {}
    for char in s:
      char_count[char] = char_count.get(char, 0) + 1
    for char in t:
      if char not in char_count or char_count[char] == 0:
        return False
      char_count[char] -= 1
    return True

solution = Solution()
test_cases = [
  ("anagram", "nagaram", True),
  ("rat", "car", False),
  ("listen", "silent", True),
]

for s, t, expected_result in test_cases:
  result = solution.isAnagram(s, t)
  print(f"Input: s='{s}', t='{t}' | Expected: {expected_result}, Result: {result}")