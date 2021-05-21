#1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i, j in enumerate(nums):
            n = target - j
            if n not in h:
                h[j] = i
            else:
                return [h[n], i]
              
 '''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
 '''
