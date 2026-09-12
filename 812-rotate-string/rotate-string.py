class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(s)

        for _ in range(n):

            e = s[-1]
            s = e + s[:-1]

            if s == goal:
                return True
        
        return False

#Brute

#Rotate string one step at a time
#After each rotation → compare with goal
#Match found? → True
#All rotations checked? → False

#TC → O(n²)
#SC → O(n)