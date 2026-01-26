class Solution:
    def findClosest(self, x, y, z):
        one = abs(z-x)
        two = abs(z-y)
        if one > two:
            return 2
        elif two > one:
            return 1
        return 0