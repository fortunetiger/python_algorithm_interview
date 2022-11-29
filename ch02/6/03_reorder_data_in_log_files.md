# Reorder Data in Log Files

[leetcode.com/problems/reorder-data-in-log-files](leetcode.com/problems/reorder-data-in-log-files)
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter, digits = [], []
        
        for log in logs:
            if log.split(' ')[1].isnumeric():
                digits.append(log)
            else:
                letter.append(log)
                
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digits
```
* Runtime: 42 ms, faster than 89.10% of Python3 online submissions for Reorder Data in Log Files.
* Memory Usage: 13.9 MB, less than 77.77% of Python3 online submissions for Reorder Data in Log Files.
