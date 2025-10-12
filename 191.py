class Solution(object):
    def hammingWeight(self, n):
        total = 0
        binary = bin(n)[2:]
        for digit in binary:
            if digit == "1":
                total += 1
        return total