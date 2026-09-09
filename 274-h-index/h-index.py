class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        # Edge Case
        if n == 1 and citations[0] == 0:
            return 0
        elif n == 1:
            return 1
        
        citations.sort()
        result = 0

        h = 1
        while h < n + 1:
            temp = []
            for num in citations:
                if num >= h:
                    temp.append(num)
            if len(temp) >= h:
                result += 1
            else:
                return result 
            h += 1
        return result

#Brute

#Try every possible h from 1 to n
#For each h, count papers with citations >= h
#At least h papers? → h is valid
#First invalid h? → stop, previous h is answer
#Sort first, but still scan all papers for every h

#TC → O(n²)
#SC → O(n)

