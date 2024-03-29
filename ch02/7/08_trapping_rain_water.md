# Trapping Rain Water
[leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

### 스택을 사용한 풀이
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break
                    
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                
            stack.append(i)
        return volume
```
* Runtime: 322 ms
* Memory Usage: 15.8 MB
