class Solution(object):
    def romanToInt(self, s):
        total = 0
        conv = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        previousnumeral = s[0]
        for numeral in s:
            if conv[numeral] <= conv[previousnumeral]:
                total += conv[numeral]
            elif conv[numeral] > conv[previousnumeral]:
                holder = conv[numeral] - conv[previousnumeral]
                total =  total + holder - conv[previousnumeral]
            previousnumeral = numeral
        return total