class Solution(object):
    def maxProfit(self, prices):
        
        differ = 0
        min_till_now = prices[0]
        for price in prices:
            differ = max(differ, price - min_till_now )
            min_till_now = min(price, min_till_now)
        return differ
