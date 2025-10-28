class Solution(object):
    def findWordsContaining(self, words, x):
        results = list()
        for word in range(len(words)):
            if x in words[word]:
                results.append(word)
        return results