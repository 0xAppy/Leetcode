# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        # LL --> Array
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        max_dist, min_dist = -1, -1
        critical_point = []

        for i in range(1,len(arr) - 1):

            # Local Minima
            if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                critical_point .append(i)
            # Local Maxima
            elif arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                critical_point .append(i)

        if len(critical_point ) > 1:
            max_dist = max(critical_point ) - min(critical_point )

            min_dist = float('inf')
        
            for i in range(1, len(critical_point )):
                temp = critical_point [i] - critical_point [i-1]
                min_dist = min(min_dist, temp)

        return [min_dist, max_dist]        

#Better

#Convert LL → array for easy neighbor checks
#Find every local min/max → mark as critical point
#Only 2+ critical points can give an answer
#Max distance = first ↔ last critical point
#Min distance = smallest gap between consecutive critical points
#Return [min distance, max distance]

#TC → O(n)
#SC → O(n)
























