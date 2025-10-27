class Solution(object):
    def numberOfBeams(self, bank):
        lasers = 0
        openlasers = 0
        for row in bank:
            ones = row.count("1")
            lasers += ones * openlasers
            if ones != 0:
                openlasers = ones
        return lasers
