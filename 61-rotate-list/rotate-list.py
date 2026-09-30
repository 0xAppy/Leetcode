# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if head is None or head.next is None:
            return head

        curr = head
        r = head
        ll_len = 1

        while curr.next:
            curr = curr.next
            ll_len += 1
            
        k = k % ll_len

        if k == 0:
            return head

        pos = ll_len - k 
        counter = 1

        while counter < pos:
            r = r.next
            counter += 1

        prev = r 

        if r.next:
            r = r.next
            h = r
            prev.next = None
        else:
            return head

        while r.next:
            r = r.next

        r.next = head

        return h

#01:20
#Optimal (Linked List)

#Find linked list length and last node
#k % length → remove unnecessary full rotations
#Find the new tail at position length - k
#Cut after new tail → next node becomes new head
#Move old tail to the old head
#Return new head

#TC → O(n)
#SC → O(1)



        
