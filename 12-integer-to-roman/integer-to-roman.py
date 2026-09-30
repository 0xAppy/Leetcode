class Solution:
    def intToRoman(self, num: int) -> str:

        value_to_roman = {
                        1: "I",
                        5: "V",
                        10: "X",
                        50: "L",
                        100: "C",
                        500: "D",
                        1000: "M"
                        }

        sep_num = [int(digit) * 10**i for i, digit in enumerate(str(num)[::-1])][::-1]

        result = ""
   
        for i in sep_num:
            i_len = len(str(i))
            base = 10 ** (i_len - 1)
            count = i // base
        
            if str(i)[0] not in "49":
                if count < 5:
                    result += value_to_roman[base] * count
                else:
                    result += value_to_roman[base*5]
                    count -= 5
                    result += value_to_roman[base] * count
                
            else:
                if str(i)[0] == "4":
                    result += value_to_roman[base] + value_to_roman[base*5]

                else:
                    result += value_to_roman[base] + value_to_roman[base*10]

        return result
        
#Better (Greedy + HashMap)

#Split number into place values → thousands, hundreds, tens, ones
#Each digit is converted using Roman numeral rules
#1–3 → repeat base symbol
#4 → base + 5× symbol, 5–8 → 5× symbol + base symbols
#9 → base + next 10× symbol
#Combine everything to form the Roman numeral

#TC → O(n)
#SC → O(n)