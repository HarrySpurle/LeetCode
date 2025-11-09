class Solution:
    def countOperations(self, num1, num2, count=0):
        if num1 == num2 == 0:
            return 0
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        count += 1
        if num1 == 0 or num2 == 0:
            return count
        return self.countOperations(num1, num2, count)
        
sol = Solution()
print(sol.countOperations(2,3))