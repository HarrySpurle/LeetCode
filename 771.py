class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels = list(jewels)
        out = 0
        for stone in stones:
            if stone in jewels:
                out += 1
        return out