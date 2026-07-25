# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])

        left  = nums[:mid]
        right = nums[mid+1:]

        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root

        
#Optimal (Recursive)

#Middle element becomes the root
#Left half builds left subtree
#Right half builds right subtree
#Repeat until no elements are left
#Choosing middle keeps the BST height balanced

#TC → O(n log n)
#SC → O(log n)  (recursion stack)