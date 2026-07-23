class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        n = len(height)
        l, r = 0, n-1

        while l != r:

            diff = r - l 
            min_h = min(height[l], height[r])
            max_area = max(max_area, diff * min_h)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1

        
        return max_area

#Optimal (Two Pointers)

#Start with widest container
#Area = width × shorter height
#Move the shorter wall inward
#Taller wall can't help if shorter wall stays the same
#Keep updating maximum area found

#TC → O(n)
#SC → O(1)