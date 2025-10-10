import re

class Solution(object):
    def strStr(self, haystack, needle):
        match = re.search(needle, haystack)
        if match != None:
            return match.start()
        else:
            return -1