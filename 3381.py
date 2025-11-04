class Solution(object):
    def findXSum(self, nums, k, x):
        currenti = 0
        result = []
        while currenti + k != len(nums) + 1:
            repeats = dict()
            sum = 0
            for element in nums[currenti:currenti+k]:
                if element in repeats:
                    repeats[element] = repeats[element] + 1
                else:
                    repeats[element] = 1
            for i in range(0,x):
                maximum = max(repeats, key=lambda k: (repeats[k], k))
                sum = sum + maximum*repeats[maximum]
                repeats[maximum] = 0
            result.append(sum)
            currenti += 1
        print(result)

sol = Solution()
sol.findXSum([1,1,2,2,3,4,2,3], 6, 2)