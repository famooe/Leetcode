#704. Binary Search

class Solution(object):
    def search(self, nums, target):       
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid_point = first + (last - first + 1) // 2
            mid_value = nums[mid_point]
            if mid_value == target:
                return mid_point
            elif target < mid_value:
                last = mid_point - 1
            else:
                first = mid_point + 1
        return -1
