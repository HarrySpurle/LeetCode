import string

class Solution(object):
    def titleToNumber(self, columnTitle):
        total = 0
        alph = [0] + list(string.ascii_uppercase)
        for index in range(len(columnTitle)):
            if index == len(columnTitle)-1:
                total += alph.index(columnTitle[index])
            else:
                total += alph.index(columnTitle[index])*(26**(len(columnTitle)-1-index))
        return total