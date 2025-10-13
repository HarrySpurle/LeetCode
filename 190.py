class Solution(object):
    def reverseBits(self, n):
        inorder = list(bin(n)[2:])
        inorder = ["0"]*(32-len(inorder)) + inorder
        reverse = ""
        for char in inorder:
            reverse = char + reverse
        return int(reverse, base=2)