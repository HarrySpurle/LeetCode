class Solution(object):
    def singleNumber(self, nums):
        numbers = dict()
        for n in nums:
            if n in numbers:
                numbers[n] += 1
            else:
                numbers[n] = 1
        for i in numbers:
            if numbers[i] == 1:
                return i
            
sol = Solution()
print(sol.singleNumber([1,2,2,3,3]))