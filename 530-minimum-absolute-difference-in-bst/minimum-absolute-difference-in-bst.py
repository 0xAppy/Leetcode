# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        abs_min = float('inf')
        prev = None

        def dfs_min(node):
            nonlocal abs_min, prev

            if not node:
                return

            dfs_min(node.left)
            
            if prev is not None:
                abs_min = min(abs_min, node.val - prev)
            
            prev = node.val
            
            dfs_min(node.right)

        dfs_min(root)
        return abs_min

# 00:32
#Optimal (Inorder DFS)

#Inorder traversal of BST gives values in sorted order
#Compare current value with previous visited value
#Difference between adjacent values → possible minimum
#Keep updating the smallest difference
#No need to store the entire inorder traversal

#TC → O(n)
#SC → O(h)  (recursion stack)