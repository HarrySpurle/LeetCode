class Solution(object):
    def lessthan(self):
        newindex = int((self.length + self.index)/2)
        self.index = newindex
        return

    def greaterthan(self):
        self.index = int((self.index)/2)
        return

    def searchInsert(self, nums, target):
        self.length = len(nums) -1
        self.index = int(self.length/2)
        if target in nums:
            while True:
                if nums[self.index] > target:
                    self.greaterthan()
                elif nums[self.index] < target:
                    self.lessthan()
                else:
                    return self.index
        else:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return self.length+1
            while True:
                    try:
                        if nums[self.index] > target:
                            self.greaterthan()
                            nums = nums[self.index:]
                        elif nums[self.index] < target:
                            self.lessthan()
                            nums = nums[:self.index]
                    except:
                        return self.index