class Solution(object):
    def singleNumber(self, nums):            
        nums_count = {}
        for i in nums:
            nums_count[i] = nums_count.get(i, 0) + 1
        for i in nums_count:
            if nums_count[i] == 1:
                return i
        
