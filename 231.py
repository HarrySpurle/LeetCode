class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        while True:
            if n == 2:
                return True
            if n % 2 == 0:
                n = n // 2
            else:
                return False