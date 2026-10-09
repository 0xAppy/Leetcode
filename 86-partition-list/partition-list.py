# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:

        left, right = ListNode(), ListNode()
        
        l_tail, r_tail = left, right
        
        while head:
            if head.val < x:
                l_tail.next = head
                l_tail = l_tail.next
            else:
                r_tail.next = ListNode(head.val)
                r_tail = r_tail.next
                
            head = head.next
        
        l_tail.next = right.next
        r_tail.next = None

        return left.next

#Better

#Two dummy lists → separate nodes into < x and >= x
#l_tail builds the left partition
#r_tail builds the right partition
#Connect left partition directly to right partition
#Still creates new nodes for the right partition
#Does not need a second traversal anymore

#TC → O(n)
#SC → O(n)  (new nodes for right partition)