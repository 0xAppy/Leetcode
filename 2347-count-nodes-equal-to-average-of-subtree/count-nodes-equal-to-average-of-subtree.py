# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        result = 0

        def traverse(root):

            nonlocal result
             
            if root is None:
                return 0, 0

            left_sum, left_len = traverse(root.left)
            right_sum, right_len = traverse(root.right)

            total_sum = root.val + left_sum + right_sum
            total_len = 1 + right_len + left_len
        
            if total_sum // total_len == root.val:
                result += 1

            return total_sum, total_len   

        traverse(root)
    
        return result

#Optimal (Postorder DFS)

#Get sum + node count from left and right subtrees
#Combine them with current node
#Average = total sum // total nodes
#Average == node value? → count it
#Return subtree sum + size upward

#TC → O(n)
#SC → O(h)  (recursion stack)

        