class Solution(object):
    def convertToBase7(self, num):
        self.base7 = ""
        if num > 0:
            self.divideBy7(num)
        elif num < 0:
            self.divideBy7(-num)
            return "-" + self.base7
        else:
            return "0"
        return self.base7

    def divideBy7(self, result):
        nextstr = str(int(result % 7))
        ans = result / 7
        if ans != 0:
            self.divideBy7(ans)
            self.base7 = self.base7 + nextstr
        else:
            self.base7 = nextstr