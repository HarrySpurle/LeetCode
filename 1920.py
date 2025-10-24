class Solution(object):
    def buildArray(self, nums):
        output = []
        #for progression in nums:
        for index in range(len(nums)):
            output.append(nums[nums[index]])
        return output

sol = Solution()
print(sol.buildArray([0,2,1,5,3,4]))