class Solution:
    def countDigits(self, num: int) -> int:

        count = 0

        split_num = list(str(num))

        for i in split_num:
            if num % int(i) == 0:
                count += 1

        return count