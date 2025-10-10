import string

class Solution(object):
    def isPalindrome(self, s):
        correcto = []
        reverseo = []
        alph = list(string.ascii_letters) + ["1","2","3","4","5","6","7","8","9","0"]

        for letter in s:
            if letter in alph:
                correcto.append(letter.lower())
        for index in range(len(s)-1, -1, -1):
            if s[index] in alph:
                reverseo.append(s[index].lower())
            
        if correcto == reverseo:
            return True
        else:
            return False
        