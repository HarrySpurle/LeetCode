class Solution(object):
    def removeElement(self, nums, val):
        index = 0
        if nums != []:
            while True:
                if nums[index] == val:
                    nums.pop(index)
                    index -= 1
                index += 1
                if index == len(nums):
                    return len(nums)
        return 0