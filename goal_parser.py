#1678. Goal Parser Interpretation

class Solution(object):
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")
      
'''
Input: command = "G()(al)"
Output: "Goal"
'''
