class Solution:
    def climbStairs(self, n):
        distinct = [1,1,2,3]
        while distinct.index(distinct[-1]) <= n:
            distinct.append(distinct[-1] + distinct[-2])
        return distinct[n]
        
    