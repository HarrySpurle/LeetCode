class Solution(object):
    def finalValueAfterOperations(self, operations):
        ops = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        x = 0
        for o in operations:
            x = x + ops[o]
        return x