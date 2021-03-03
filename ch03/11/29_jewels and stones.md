```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        freq = collections.defaultdict(int)
        for s in stones:
            freq[s] += 1
            
        output = 0
        for j in jewels:
            output += freq[j]
        
        return output
```
Runtime: 24 ms, faster than 31.56% of Python online submissions for Jewels and Stones.
Memory Usage: 13.6 MB, less than 8.28% of Python online submissions for Jewels and Stones.
