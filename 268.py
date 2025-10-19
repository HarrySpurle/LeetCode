class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            print(i)
            if i not in nums:
                return i