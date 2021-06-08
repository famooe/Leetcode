class Solution(object):
    def isHappy(self, n):
        meet = set()
        
        while n not in meet:
            meet.add(n)
            n = self.someOfSquares(n)
            
            if n == 1:
                return True
        return False
    
    def someOfSquares(self, n):
        output = 0    
        
        while n:
            reminder = n % 10
            reminder = reminder*reminder            
            output = output + reminder
            n = n // 10
        return output
