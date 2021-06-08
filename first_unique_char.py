class Solution(object):
    def firstUniqChar(self, s):
        count = collections.Counter(s)
        
        for index , char in enumerate(s):
            if count[char] == 1:
                return index
            
        return -1
