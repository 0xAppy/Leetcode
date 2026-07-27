class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low,high = 0,n-1
        first,last = -1,-1 
        first_occur = float(inf)
        last_occur = float(-inf)
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                first = mid 
                first_occur = min(first_occur,first)
                first = first_occur
                high = mid - 1
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1

        low,high = 0,n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                last = mid 
                last_occur = max(last_occur,last)
                last = last_occur
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        return [first,last]
            
