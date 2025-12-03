from math import log

class Solution:
    def isPowerOfFour(self, n):
        if n <= 0: return False
        x = log(n,4)
        if 4**int(x) == n and (x == 0 or x >= 1) : return True
        else: return False