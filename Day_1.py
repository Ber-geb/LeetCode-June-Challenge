# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        swapGivenLevel(root, 1) #call function
        return root 

def swapGivenLevel(root, level): #swap the given level nodes
    if (root is None or (root.left is None and root.right is None)):
        return

    root.left, root.right = root.right, root.left # perform swap

    swapGivenLevel(root.left, level + 1) #traverse tree from left node
    swapGivenLevel(root.right, level + 1)#traverse tree from right node





        