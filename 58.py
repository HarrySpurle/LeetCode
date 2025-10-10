class Solution(object):
    def lengthOfLastWord(self, s):
        listed = list(s)
        length = 0
        started = 0
        for index in range (len(listed)-1,-1,-1):
            if started == 0 and listed[index] == " ":
                pass
            if listed[index] != " ":
                started = 1
                length += 1
            if started == 1 and listed[index] == " ":
                return length
        return length