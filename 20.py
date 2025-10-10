class Solution(object):
    def isValid(self, s):
        alph = {"[":1, "]":-1, "{":1,"}":-1,"(":1,")":-1 }
        square = [["[","]"],0]
        curly = [["{","}"],0]
        round = [["(",")"],0]
        order = []

        for char in s:
            if char in square[0]:
                square[1] += alph[char]
                if char == "[":
                    order.append("s")
                elif order == []:
                    return False
                elif order[-1] == "s":
                    order.pop()
                else:
                    return False
            if char in curly[0]:
                curly[1] += alph[char]
                if char == "{":
                    order.append("c")
                elif order == []:
                    return False
                elif order[-1] == "c":
                    order.pop()
                else:
                    return False
            if char in round[0]:
                round[1] += alph[char]
                if char == "(":
                    order.append("r")
                elif order == []:
                    return False
                elif order[-1] == "r":
                    order.pop()
                else:
                    return False
        if square[1] == 0 and curly[1] == 0 and round[1] == 0:
            return True
        else:
            return False

sol = Solution()
print(sol.isValid("([)]"))