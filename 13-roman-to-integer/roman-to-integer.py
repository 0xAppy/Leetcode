class Solution:
    def romanToInt(self, s: str) -> int:

        n = len(s)

        roman = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

        result = 0   
        prev = 0

        for ch in range(n-1, -1, -1):
            curr = roman[s[ch]]

            if prev > curr:
                result -= curr
            else:
                result += curr
            
            prev = curr
        
        return result

#Optimal (HashMap + Greedy)

#Read Roman numerals from right to left
#Current value smaller than previous? → subtract it
#Otherwise → add it
#Update prev to current value
#Subtractive cases like IV, IX, XL work automatically

#TC → O(n)
#SC → O(1)