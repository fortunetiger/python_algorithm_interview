### 1회 시도
```python
class Solution(object):
    def groupAnagrams(self, strs):

        groups = {}
        for word in strs :
            ana = str(''.join(sorted(word)))
            if ana in groups.keys() : groups[ana].append(word)
            else :
                groups[ana] = []
                groups[ana].append(word)
                
        return groups.values()
```
Runtime: 1192 ms<br>
Memory Usage: 17.2 MB<br>
- dictionary 초기화하지 않고 시작, key 유무판정이 들어가서 느림. 매우느림...
- unicode에 str씌우는거 빼버림(불필요)<br>

### 2회 시도
```python
class Solution(object):
    def groupAnagrams(self, strs):

        groups = collections.defaultdict(list)
        for word in strs :
            groups[''.join(sorted(word))].append(word)
                
        return groups.values()
```
Runtime: 84 ms, faster than 75.97% of Python online submissions for Group Anagrams.<br>
Memory Usage: 17.7 MB, less than 53.77% of Python online submissions for Group Anagrams.<br><br>
