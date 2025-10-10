class Solution(object):
    def addBinary(self, a, b):
        result = []
        carry = 0
        alist, blist = list(a), list(b)

        if len(alist) < len(blist):
            alist = ["0"] * (len(blist) - len(alist)) + alist
        else:
            blist = ["0"] * (len(alist) - len(blist)) + blist

        for i in range(len(alist) - 1, -1, -1):
            adig, bdig = int(alist[i]), int(blist[i])
            total = adig + bdig + carry
            result.insert(0, str(total % 2))
            carry = total // 2

        if carry == 1:
            result.insert(0, "1")

        return "".join(result)