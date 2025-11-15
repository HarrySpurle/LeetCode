from math import log

class Solution:
    def isPowerOfFour(self, n):
        if n <= 0: return False
        x = log(n,4)
        print(int(4**x) == n)
        if int(4**x) == n and (x == 0 or x >= 1) : return True
        else: return False
        
sol = Solution()
print(sol.isPowerOfFour(6))