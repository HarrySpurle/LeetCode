class Solution(object):
    def addDigits(self, num):
        result = self.sum(num)
        return result
    
    def sum(self,num):
        num = list(str(num))
        total = 0
        for element in num:
            total += int(element)
        if total >= 10:
            total = self.sum(total)
        return total