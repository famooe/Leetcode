class Solution(object):
    def climbStairs(self, n):
        c = 0
        f = [1,2]
        for i in range(2, n):
            f.append(f[i - 2] + f[i - 1])
            
        return f[n - 1]
