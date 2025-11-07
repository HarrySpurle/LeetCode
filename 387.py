class Solution(object):
    def firstUniqChar(self, s):
        letterreps = dict()
        for letter in s:
            if letter in letterreps:
                letterreps[letter] = letterreps[letter] + 1
            else:
                letterreps[letter] = 1
        minimum = min(letterreps, key=letterreps.get)
        if letterreps[minimum] == 1:
            print(s.index(minimum))
            return s.index(minimum)
        return -1     