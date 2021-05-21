#1436. Destination City

class Solution(object):
    def destCity(self, paths):
        return ({path[1] for path in paths} - {path[0] for path in paths}).pop()
      
'''
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
'''
