class Solution:
    def differenceOfSums(self, n, m):
        return sum(i for i in range(0, n+1) if i%m!=0) - sum(i for i in range(0, n+1) if i%m==0)
    
sol = Solution()
print(sol.differenceOfSums(10,3))
        