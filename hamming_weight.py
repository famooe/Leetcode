class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        while n:
            n = n & (n-1)
            counter += 1
        return counter
