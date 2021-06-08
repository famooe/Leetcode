# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))
        output = []
        if root:
            output = self.inorderTraversal(root.left)
            output.append(root.val)
            output = output + self.inorderTraversal(root.right)
        return output
        
