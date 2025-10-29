class Solution(object):
    def smallestNumber(self, n):
        binary = str(bin(n)[2:])
        binary = binary.replace("0","1")
        return int(binary, base = 2)