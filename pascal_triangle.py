class Solution(object):
    def generate(self, numRows):
        output = [[] for i in range (numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j < i :
                    if j == 0:
                        output[i].append(1)
                    else:
                        output[i].append(output[i-1][j] + output[i-1][j-1])
                        
                elif j == i:
                    output[i].append(1)
                
        return output
