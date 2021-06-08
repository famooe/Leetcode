class Solution(object):
    def firstUniqChar(self, s):
        count = collections.Counter(s)
        # print(count.items())            # is a list=[(char1, iter1), (char2, iter2), ...]
        for index , char in enumerate(s):
            if count[char] == 1:
                return index
            
        return -1
