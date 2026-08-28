class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        max_words = 0

        for sentence in sentences:
            sentence = sentence.split()
            max_words = max(max_words, len(sentence))

        return max_words
        
## EASY PEASYY!