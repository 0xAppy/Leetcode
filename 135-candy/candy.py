class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        s = [1] * n

        # Left --> Right

        for i in range(n):
            if i-1 >= 0:
                if ratings[i] > ratings[i-1]:
                    s[i] = s[i - 1] + 1

        # Right --> Left

        for i in range(n-1, -1, -1):
            if i+1 < n:
                if ratings[i] > ratings[i+1]:
                    s[i] = max(s[i], s[i + 1] + 1)

        return sum(s)

#Better (Greedy)

#Start everyone with 1 candy
#Left → Right: higher rating than left → give +1
#Right → Left: higher rating than right → give +1
#Use max() to preserve both-side requirements
#Sum candies for the minimum valid distribution

#TC → O(n)
#SC → O(n) (O(1) for Optimal)