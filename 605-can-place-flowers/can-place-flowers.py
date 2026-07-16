class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        planted = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                left_empty = (i == 0 or flowerbed[i - 1] == 0) #prev
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) #nxt

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    planted += 1

        return planted >= n

#Optimal (Greedy)

#Check only empty plots
#Can plant only if both neighbors are empty (or boundary)
#Plant immediately when possible
#Update flowerbed to avoid adjacent planting later
#Count planted flowers and compare with n

#TC → O(n)
#SC → O(1)