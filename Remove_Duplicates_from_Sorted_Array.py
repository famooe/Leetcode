class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                nums.pop(i)
            i += 1
        return len(nums)
