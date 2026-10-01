# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        l1_arr, l2_arr = [], []
        
        # optimize
        while l1 or l2:
            if l1:
                l1_arr.append(l1.val)
                l1 = l1.next

            if l2:
                l2_arr.append(l2.val)
                l2 = l2.next
        
        print(l1_arr,l2_arr)

        num1 = int("".join(map(str, l1_arr))[::-1])
        num2 = int("".join(map(str, l2_arr))[::-1])

        print(num1, num2)

        num_sum = num1+num2
        print(num_sum)

        digits = list(map(int, str(num_sum)[::-1]))

        sum_node = ListNode(0)
        curr = sum_node # head

        for digit in digits:
            curr.next = ListNode(digit)
            curr = curr.next

        return sum_node.next

# 00:23
#Better

#Convert both linked lists into arrays
#Reverse digits → rebuild the actual numbers
#Add the two numbers normally
#Reverse sum digits → create the result linked list
#Works, but uses extra arrays + integer conversion

#TC → O(n + m)
#SC → O(n + m)






        