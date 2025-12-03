class Solution:
    def isIsomorphic(self, s, t):
        mappingss = dict()
        mappingst = dict()
        seenletterss = []
        seenletterst = []
        for index in range(len(s)):
            if s[index] not in seenletterss:
                mappingss[s[index]] = t[index]
                seenletterss.append(s[index])
            else:
                if mappingss[s[index]] != t[index]:
                    return False
        for index in range(len(s)):
            if t[index] not in seenletterst:
                mappingst[t[index]] = s[index]
                seenletterst.append(t[index])
            else:
                if mappingst[t[index]] != s[index]:
                    return False
        return True
        