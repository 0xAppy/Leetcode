class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if head is None or left == right:
            return head

        curr, tail = head, head
        l_count, r_count = 1, 1

        # Find left node
        while l_count < left:
            curr = curr.next
            l_count += 1

        # Find right node
        while r_count < right:
            tail = tail.next
            r_count += 1

        prev_node = None
        start = curr
        after = tail.next

        # Reverse left -> right
        while curr != after:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        # Reconnect
        if left == 1:
            head = prev_node
        else:
            prev = head

            for _ in range(left - 2):
                prev = prev.next

            prev.next = prev_node

        start.next = after

        return head
