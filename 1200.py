class Solution(object):
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        mindiff = arr[1]-arr[0]
        pairs = []
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff == mindiff:
                pairs.append([arr[i],arr[i+1]])
            elif diff < mindiff:
                mindiff = diff
                pairs = [arr[i],arr[i+1]]
        if len(pairs) == 1: return pairs[0]
        else: return pairs 

sol = Solution()
print(sol.minimumAbsDifference([40,11,26,27,-20]))