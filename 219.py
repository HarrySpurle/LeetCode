class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = dict()
        dupval = list()
        indicies = list()
        for item in nums:
            if item in seen:
                seen[item] += 1
            else:
                seen[item] = 1
        for element in seen:
            if seen[element] >= 2:
                dupval.append(element)
        for i in range(len(nums)):
            if nums[i] in dupval:
                indicies.append(i)
        for a in indicies:
            for b in indicies:
                if a != b and abs(a-b) <= k and nums[a] == nums[b]:
                    return True
        return False
    
