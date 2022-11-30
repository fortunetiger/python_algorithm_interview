# Two Sum
[leetcode.com/problems/two-sum](leetcode.com/problems/two-sum)
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

* Runtime: 116 ms
* Memory Usage: 13.3 MB

2022-11-30
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            c = target-n
            if c in nums[i+1:]:
                return [i, nums[i+1:].index(c)+(i+1)]
```
* Runtime: 766 ms, faster than 28.69% of Python3 online submissions for Two Sum.
* Memory Usage: 14.9 MB, less than 96.12% of Python3 online submissions for Two Sum.
