# Most Common Word
[leetcode.com/problems/most-common-word](leetcode.com/problems/most-common-word)
```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        words = re.split('[!?\',;. ]', str(paragraph).lower())           
        dic = set(words)                 
                       
        maximum = 0
        answer = ""
        for word in dic:
            if word == '' or (word in banned) : continue
            else :
                if  words.count(word) > maximum :
                    maximum = words.count(word)
                    answer = word
        
        return answer
```

* Runtime: 20 ms, faster than 93.01% of Python online submissions for Most Common Word.
* Memory Usage: 13.6 MB, less than 68.80% of Python online submissions for Most Common Word.

2022-11-29
```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned.append('')
        paragraph = re.split('[!?\',;. ]', str(paragraph).lower())
        counter   = collections.Counter(paragraph)
        
        for word in banned:
            try:
                counter.pop(word)
            except(KeyError):
                pass
        
        return counter.most_common(1)[0][0]
```
* Runtime: 69 ms, faster than 52.44% of Python3 online submissions for Most Common Word.
* Memory Usage: 13.9 MB, less than 37.10% of Python3 online submissions for Most Common Word.
