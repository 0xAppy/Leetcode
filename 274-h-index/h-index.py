class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(n):
            h = n - i

            if citations[i] >= h:
                return h
        
        return 0

#Optimal (Sorting + Greedy)

#Sort citations → smallest to largest
#At index i → there are n-i papers with at least this many citations
#h = n-i → required number of papers
#citations[i] >= h? → valid h-index found
#First valid h while scanning left → maximum possible h

#TC → O(n log n)
#SC → O(1) (ignoring sorting space)