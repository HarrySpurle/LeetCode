class Solution(object):
    def moveZeroes(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                index -= 1
            index += 1
        return nums