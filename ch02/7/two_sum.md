```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def index_all(nums, x):
            result =[]
            for i in range(0, len(nums)) :
                if nums[i] == x : result.append(i)
            return result
        
        if len(nums) == 2 : return [0, 1]
        
        while True :
            num = random.choice(nums)
            if target-num != num and (target-num) in nums :
                return [nums.index(num), nums.index(target-num)]

            else :
                if nums.count(num) == 2 :
                    return index_all(nums, num)
```
무식하게 풂

Runtime: 116 ms

Memory Usage: 13.3 MB

