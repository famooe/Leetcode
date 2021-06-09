class Solution(object):
    def majorityElement(self, nums):
        maj_count = len(nums) // 2
        item_count = {}
        for item in nums:
            item_count[item] = item_count.get(item, 0) + 1
            if item_count[item] > maj_count:
                return item
