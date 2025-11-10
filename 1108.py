class Solution:
    def defangIPaddr(self, address):
        index = 0
        while index != len(address):
            if address[index] == '.':
                address = address[:index] + '[.]' + address[index+1:]
                index += 3
            index += 1
        return address