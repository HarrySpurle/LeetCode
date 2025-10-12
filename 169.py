class Solution(object):
    def majorityElement(self, nums):
        elements = dict()
        for el in nums:
            if el in elements:
                elements[el] += 1
            else:
                elements[el] = 1
        return max(elements, key=elements.get)