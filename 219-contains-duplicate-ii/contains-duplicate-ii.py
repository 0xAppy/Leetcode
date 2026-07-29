class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(nums) == 1:
            return False

        window = set()

        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


#Optimal (Sliding Window + HashSet)

#Window stores last k elements
#Duplicate inside window? → return True
#Window exceeds size k? → remove leftmost element
#Keep sliding the window forward
#No duplicate found within k distance → return False

#TC → O(n)
#SC → O(min(n, k))