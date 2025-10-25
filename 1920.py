class Solution(object):
    def buildArray(self, nums):
        output = []
        for index in range(len(nums)):
            output.append(nums[nums[index]])
        return output