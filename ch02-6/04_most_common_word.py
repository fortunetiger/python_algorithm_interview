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

## Runtime: 20 ms, faster than 93.01% of Python online submissions for Most Common Word.
## Memory Usage: 13.6 MB, less than 68.80% of Python online submissions for Most Common Word.
