# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Edge Case
        if head is None:
            return head
        if head.next is None:
            return None
        current = head
        prev_node = None
        count = 0
        #len of SLL
        len_l = 0
        while current:
            current = current.next
            len_l += 1
        current = head
        
        index = len_l - n
        while count < index and current:
            prev_node = current
            current = current.next
            count += 1
        if index == 0:
            return head.next
        else:
            prev_node.next = current.next
        return head
