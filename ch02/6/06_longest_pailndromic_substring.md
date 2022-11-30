# Longest Pailndromic Substring
[leetcode.com/problems/longest-palindromic-substring](leetcode.com/problems/longest-palindromic-substring)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left:int, right:int) -> str:
            while (left >= 0) and (right <= len(s)) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1 : right-1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        
        for i in range(len(s)-1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
            
        return result
```
* Runtime: 430 ms, faster than 93.66% of Python3 online submissions for Longest Palindromic Substring.
* Memory Usage: 14 MB, less than 30.26% of Python3 online submissions for Longest Palindromic Substring.
