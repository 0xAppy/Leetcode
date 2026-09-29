class Solution:
    def frequencySort(self, s: str) -> str:

        my_dict = {}

        # getting elements in dict
        for ch in s:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        # Sorting dict as per value
        sorted_dict = dict(sorted(my_dict.items(), key = lambda x: x[1]))

        result = []

        # Adding elements
        for key, count in sorted_dict.items():
            result.extend([key] * count)

        result = "".join(result)

        return result[::-1]

#Better (HashMap + Sorting)

#Count frequency of every character
#Sort characters by frequency
#Build result using each character's count
#Reverse at the end → highest frequency comes first

#TC → O(n log n)
#SC → O(n)