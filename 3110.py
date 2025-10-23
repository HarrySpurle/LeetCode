class Solution(object):
    def scoreOfString(self, s):
        vals = []
        p1 = 0
        p2 = 1
        diff = 0
        for char in s:
            vals.append(ord(char))
        while p1 < len(vals)-1 and p2 < len(vals):
            diff = diff + abs(vals[p1]- vals[p2])
            p1 += 1
            p2 +=1
        return diff

        

sol = Solution()
print(sol.scoreOfString("hello"))