class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0

        result = 0
        n = len(height)
        l, r = 0, n-1

        # Max Left and Right
        temp_l = 0
        max_left = [0]
        temp_r = 0
        max_right = [0]
        i = 0

        while i<len(height):

            max_left.append(max(max(max_left), temp_l))
            temp_l = height[i]

            max_right.append(max(max(max_right), temp_r))
            temp_r = height[(n-1) - i]

            i+= 1
        max_left.pop(0)
        max_right.pop(0)
        max_right.reverse()

        temp = 0
        for i in range(len(height)):
            temp = min(max_left[i], max_right[i]) - height[i]

            if temp > 0:
                result += temp  

        return result

#Better (Prefix & Suffix Max)

#Precompute tallest bar on left and right
#Water level = shorter of leftMax and rightMax
#Current bar blocks some water
#Trapped water = water level - current height
#Add water only if it's positive

#TC → O(n)
#SC → O(n)
    