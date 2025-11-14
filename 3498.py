class Solution:
    def reverseDegree(self, s):
        result = 0
        for index in range(len(s)):
            position = ord(s[index]) -97
            result += (index+1)*(26-position)
        return result