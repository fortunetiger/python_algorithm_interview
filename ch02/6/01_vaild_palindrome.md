```python
class Solution(object):
    
    def is_alphanumeric(self, c):
        return (c.isalpha()) or (c.isdigit())
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = str(s)
        s = filter(self.is_alphanumeric,s).lower()
        
        if len(s) <= 1: return True
        
        for i in range(0, len(s)):
            if (s[i] != s[-(i+1)]):return False
            if i>= (len(s)/2):return True
```
            
* Runtime: 48 ms, faster than 49.21% of Python online submissions for Valid Palindrome.
* Memory Usage: 16 MB, less than 12.82% of Python online submissions for Valid Palindrome.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(list(filter(str.isalnum, s)))
        s = s.lower()
        
        for i in range(0, len(s)//2):
            if s[i] != s[len(s)-(i+1)]:
                return False
        return True
```
* Runtime: 46 ms, faster than 94.96% of Python3 online submissions for Valid Palindrome.
* Memory Usage: 14.6 MB, less than 45.56% of Python3 online submissions for Valid Palindrome.
