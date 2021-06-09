class Solution(object):
    def romanToInt(self, s):
        alphabet = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        output = 0
        
        for each in range(len(s)):
            if ((each+1) != len(s)) and (alphabet[s[each]] < alphabet[s[each + 1]]):
                output -= alphabet[s[each]]
            else:
                output += alphabet[s[each]]
                 
        return output
                
