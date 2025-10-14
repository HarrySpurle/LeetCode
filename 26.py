class Solution(object):
    def removeDuplicates(self, nums):
        index = 1
        if len(nums) == 1:
            return 1
        while True:
            if nums[index] == nums[index-1]:
                
                nums.pop(index)
                index -= 1
            if index == len(nums)-1:
                break
            index += 1
        return len(nums)