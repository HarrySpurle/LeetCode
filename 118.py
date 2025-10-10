class Solution(object):
    def generate(self, numRows):
        pascal = [[1]]
        row = 2
        newrow = [1]
        while row <= numRows:
            for i in range(1,len(pascal[-1])):
                newrow.append(pascal[-1][i-1] + pascal[-1][i])
            newrow.append(1)
            row += 1
            pascal.append(newrow)
            newrow = [1]
        return pascal