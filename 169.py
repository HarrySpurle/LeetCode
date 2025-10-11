class Solution(object):
    def majorityElement(self, nums):
        elements = dict()
        for el in nums:
            if el in elements:
                elements[el] += 1
            else:
                elements[el] = 1
        print(elements)
        return max(elements, key=elements.get)

sol = Solution()
print(sol.majorityElement([3,3,4])) 
