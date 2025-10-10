class Solution(object):
    def plusOne(self, digits):
        number = ""
        for i in digits:
            number = number + str(i)
        result = int(number) + 1
        newlist = list(str(result))
        for i in range(len(newlist)):
            newlist[i] = int(newlist[i])
        return newlist