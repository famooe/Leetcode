class Solution(object):
    def maxSubArray(self, nums):
        best_sum = nums[0]
        current_sum = 0
        
        for x in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
            
            current_sum = current_sum + nums[x]
            best_sum = max(best_sum, current_sum)
        return best_sum
