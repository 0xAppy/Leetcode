# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return None

        temp_list = ListNode(0, head)
        
        prev = temp_list
        curr = head

        while curr and curr.next:

            if curr.val == curr.next.val:
                temp = curr.val

                while curr and curr.val == temp:
                    curr = curr.next 

                prev.next =curr

            else:
                prev = curr
                curr = curr.next


        return temp_list.next

# 00:33
#Optimal (Two Pointers)

#Dummy node keeps the head handling simple
#curr scans through the sorted linked list
#Duplicate found? → skip the entire duplicate group
#prev.next = curr → remove duplicates by reconnecting links
#No duplicate? → move prev and curr forward
#Return dummy.next as the cleaned list

#TC → O(n)
#SC → O(1)

        