class Solution(object):
    def containsDuplicate(self, nums):
        seen = dict()
        for item in nums:
            if item in seen:
                seen[item] += 1
            else:
                seen[item] = 1
        if seen[max(seen, key=seen.get)] >=2:
            return True
        return False